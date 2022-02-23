"""
Python library for the codectrl-logger program.

This library has a single logging function that upon being
called, collects information about the callee and the environment.
The function then sends this information to the codectrl server.

More information on this can be found at:
https://github.com/Authentura/codectrl/
"""


import sys
import json
import socket
import inspect
import cbor2


class Log:
    """
        On initialisation the logger class formats data passed
        to it and other wise collected data to create a json and cbor
        object as described by https://github.com/pwnCTRL/codectrl/blob/main/loggers/SCHEMA.md
    """
    def __init__(self, surround: int,  *args, **kwargs):
        """
            The __init__ function does most of the
            work in this class as we don't want to
            separately run a method of each log.
        """
        # Warning message if anything goes wrong
        self.warning: list[str] = []

        # Set the message type based on the included arguments.
        # If there is only one argument then set
        # the message type to the type of the single argument.
        # If there are more arguments then set it to the string "list"
        self.message_type: str = (str(type(args[0])) if len(args) == 1 else "list")

        # Get the message arguments
        # These 2 functions set the append the messages
        # to the `message` instance variable.
        self.message: str = ""
        self._normalise_args(*args)
        self._normalise_kwargs(**kwargs)


        # Format and assign the stack
        self.stack: list[dict[str, str|int]] = []
        self._get_stack()

        # Get and set filename
        self.file_name: str = ""
        self._get_caller_file_name()

        # get line number
        self.line_number: int = 0
        self._get_caller_line_number()

        # get code_snippet
        self.code_snippet: dict[str,str] = {}
        self._get_code_snippet(surround)



    def _normalise_args(self, *args) -> None:
        """ Create a string out of *args """
        for argument in args:
            self.message+= str(argument) + "  "



    def _normalise_kwargs(self, **kwargs) -> None:
        """ Create a string out of **kwargs** """
        for key, val in kwargs.items():
            self.message += f"{key}='{val}'  "



    def _get_stack(self) -> None:
        """
            Set self.stack to the stack according to the following specifications:
            https://github.com/pwnCTRL/codectrl/blob/main/loggers/SCHEMA.md
        """

        stack: list[dict[str, str|int]] = []
        for stack_entry in inspect.stack():

            # code_context is doesn't always exist, not exactly sure why.
            if stack_entry.code_context is not None:
                code: str = stack_entry.code_context[0].strip().strip("\n")
            else:
                code = "None"

            stack.append({
                    "code":          code,
                    "name":          stack_entry.function,
                    "file_path":     stack_entry.filename,
                    "line_number":   stack_entry.lineno,
                    "column_number": 0,
                    })

        # Reverse the stack as it should be FIFO
        stack = stack[::-1]

        # Remove all calls from the stack that happened from
        # within the logging function. If there is a new function
        # added before calling stack.inspect() then add an extra
        # stack.pop() accordingly.
        stack.pop()
        stack.pop()
        stack.pop()

        self.stack = stack



    def _get_caller_file_name(self) -> None:
        """ Get filename of the caller function """
        self.file_name = inspect.stack()[3].filename

    def _get_caller_line_number(self) -> None:
        """ Get filename of the caller function """
        self.line_number = inspect.stack()[3].lineno


    def _get_code_snippet(self, surround: int) -> None:
        """
            Function gets {surround} number of lines
            of code from above and below the line that
            called codectrl.log.

            This helps the person working with the code
            to debug and quickly identify where it is
            coming from.
        """

        try:
            with open(self.file_name, "r", encoding='utf-8')as ifstream:
                source_code = ifstream.read().split('\n')

        except Exception as err: # pylint: disable=broad-except # This needs to be broad.
            self.warning.append(f"An error occurred in library file while reading code: {err}")
            return


        ## get only the {surround} above and below the log call
        useful_lines: dict[str,str] = {}
        for i in range(self.line_number-surround, self.line_number+surround):
            try:
                # Just ignore values where i < 0
                if i >= 0:
                    # plus 1 is added, as most IDE's start count
                    # at 1, whereas python starts at 0
                    useful_lines[str(i+1)] = source_code[i]
            except IndexError:
                # Can ignore this error as it
                # likely just means that there
                # are no more lines in the file.
                pass

        self.code_snippet = useful_lines


    def json(self) -> dict:
        """ Return all data collected as json """

        return {
                "message"      : self.message,
                "message_type" : self.message_type,
                "line_number"  : self.line_number,
                "code_snippet" : self.code_snippet,
                "file_name"    : self.file_name,
                "stack"        : self.stack,
                "warnings"     : self.warning,
                "address"      : "127.0.0.1" # temp
                }


    def cbor(self) -> bytes:
        """ Returns cbor string of collected data """
        return cbor2.dumps(self.json())





def log(*args, host="127.0.0.1", port=3001, surround=3, **kwargs) -> bool:
    """
        Create `Log` object and send to codeCTRL server in cbor format.

        The codectrl.log function collects and formats information about
        the file/function/line of code it got called on and sends it to
        the codeCTRL server, if available.


        Usage:
            The function takes any number of positional
            or keyword arguments of all types.

            All positional arguments get included in the log `message`
            using str() or json.dumps(obj, indent=4) in case of dicts.

            Keyword arguments, other than `reserved` ones, get appended
            to the logs as {key}={value}


        Reserved arguments:
            * host:
                By default set to `127.0.0.1`, this argument
                holds the address of the codeCTRL server.

            * port:
                By default set to `30001`, this is the port
                the codeCTRL server should be contacted at.

            * surround:
                By default `3`, this argument specifies the
                number of lines of code that should be displayed
                around the call to `codectrl.log`.
    """

    # This makes it easier for users of the library
    # to debug errors they caused.
    assert isinstance(host, str), "host variable has to be a string"
    assert isinstance(port, int), "port variable has to be an integer"
    assert isinstance(surround, int), "surround variable has to be an integer"

    # Try connect to the server.
    try:
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soc.connect((host, port))
    except Exception as err: # pylint: disable=broad-except # Could be many things.
        print(f"[codeCTRL] Could not reach codeCTRL server. {err}", file=sys.stderr)
        return False

    # Collect logging data
    log_obj: Log = Log(surround, *args, **kwargs)

    # Send logging data to server
    soc.send(log_obj.cbor())
    # s.send(b'\0')

    # close socket
    soc.close()
    return True
