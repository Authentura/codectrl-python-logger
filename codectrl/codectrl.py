import sys
import json
import traceback

from pprint import pprint


class Log:
    """
        On initialisation the logger class formats data passed
        to it and other wise collected data to create a json and cbor
        object as described by https://github.com/pwnCTRL/codectrl/blob/main/loggers/SCHEMA.md
    """
    def __init__(self,  *args, **kwargs):
        """
            The __init__ function does most of the
            work in this class as we dont want to
            seperately run a method of each log.
        """

        # format and normalise the message
        self.message = self._normalise_args(*args) + self._normalise_kwargs(**kwargs)

        print(self.message)
        print()
        print()

        self.stack = self._get_stack()



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
            string += f"{k}='{v}'m   "
        return string


    def _format_stack_entry(self, call: object) -> dict:
        """
            Fromats a single stack entry according to:
            https://github.com/pwnCTRL/codectrl/blob/main/loggers/SCHEMA.md
        """
        # print(call)
        # print(dir(call))

        # exc_type, exc_value, exc_traceback = 
        pprint(dir(call[0]))

        print("code: ", dir(call[0]))
        print("code: ", call[0].__str__())

        stack_entry = {
                "file_name": call[0].f_code.co_filename,
                }

        print()
        pprint(stack_entry)
        return stack_entry


    def _get_stack(self) -> list:
        """ Get the current call stack formatted """
        stack = list(traceback.format_stack())

        # Remove the last 2 entries
        # as they are internal to this
        # library
        stack.pop()
        stack.pop()
        formated_stack = []

        for call in traceback.walk_stack(None):
            self._format_stack_entry(call)
            break

        return formated_stack
