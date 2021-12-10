import sys
import json
import cbor2
import socket
import inspect


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
        self.warning = []

        # format and normalise the message
        self.message_type = "&str"
        self.message = self._normalise_args(*args) + self._normalise_kwargs(**kwargs)


        # format the stack
        self.stack        = self._get_stack()
        # get file_name
        self.file_name    = self._get_caller_file_name()
        # get line number
        self.line_number  = self._get_caller_line_number()
        # get code_snippet
        self.code_snippet = self._get_code_snippet(surround)



    def _normalise_args(self, *args) -> str:
        """ Create a string out of *args """
        string = ""
        for argument in args:
            string += str(argument) + "  "
        return string



    def _normalise_kwargs(self, **kwargs) -> str:
        """ Create a string out of **kwargs** """
        string = ""
        for k, v in kwargs.items():
            string += f"{k}='{v}'  "
        return string



    def _get_stack(self) -> list:
        """
            Get the current stack and format it according to spec:
            https://github.com/pwnCTRL/codectrl/blob/main/loggers/SCHEMA.md
        """

        stack = []
        for stack_entry in inspect.stack():
            stack.append({
                    "name":          stack_entry.function,
                    "code":          (stack_entry.code_context[0].strip().strip("\n") if stack_entry.code_context != None else "None"),
                    "file_path":     stack_entry.filename,
                    "line_number":   stack_entry.lineno,
                    "column_number": 0,
                    })

        # Reverse the stack as it should be FIFO
        stack = stack[::-1]

        # remove the functions called inside this module
        stack.pop()
        stack.pop()
        stack.pop()

        return stack



    def _get_caller_file_name(self) -> str:
        """ Get filename of the caller function """
        return inspect.stack()[3].filename

    def _get_caller_line_number(self) -> str:
        """ Get filename of the caller function """
        return inspect.stack()[3].lineno


    def _get_code_snippet(self, surround: int) -> dict:
        """
            Get a {surround} lines above and below
            the line of code calling log
        """

        try:
            with open(self.file_name, "r")as ifstream:
                source_code = ifstream.read().split('\n')

        except Exception as e:
            self.warning.append(f"An error occurred in library file while reading code: {e}")
            return []

        ## get only the {surround} above and below the log call
        useful_lines = {}
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

        return useful_lines


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


    def cbor(self) -> str:
        """ Returns cbor string of collected data """
        return cbor2.dumps(self.json())





def log(*args, host="127.0.0.1", port=3001, surround=3, **kwargs) -> int:
    """
        Create `Log` object and send to codeCTRL server in cbor format.

        The codectrl.log function collects and formats information about
        the file/function/line of code it got called on and sends it to
        the codeCTRL server, if available.


        Usage:
            The function takes any number of arbitrary positional
            and keyword arguments. 

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
    assert type(host)     == str, "host variable has to be a string"
    assert type(port)     == int, "port variable has to be an integer"
    assert type(surround) == int, "surround variable has to be an integer"

    # Try connect to the server.
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('127.0.0.1', 3001))
    except Exception as e:
        print(f"An error occurred while codeCTRL logger was trying to connect to server: {e}", file=sys.stderr)
        sys.exit(-1)

    # Collect logging data
    log_obj = Log(surround, *args, **kwargs)

    # Send logging data to server
    s.send(log_obj.cbor())
    # s.send(b'\0')

    # close socket
    s.close()



