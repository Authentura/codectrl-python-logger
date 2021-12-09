codeCTRL (python)
===============

A python library for the [codeCTRL](https://github.com/pwnCTRL/codeCTRL) logger.

The `codectrl.log` function collects and formats information about
the file/function/line of code it got called on and sends it to
the codeCTRL server, if available.

Installation
------------

### pip
```
pip install codectrl
```

### Manual install (linux & MacOS)

Clone the repository:
```
git clone https://github.com/pwnCTRL/codectrl-python-logger.git
cd codectrl-python-logger
```
Build the package:
```
python3 setup.py build
```
Install the package.
Depending on your python install this may require root privileges.
```
(sudo) python3 setup.py install
```


Usage
-----
Make sure you have the [codeCTRL](https://github.com/pwnCTRL/codeCTRL) application running.

Anywhere in a python codebase you can insert `codectrl.log()` to print logs to the codeCTRL app.


The function takes any number of arbitrary positional
and keyword arguments. 

All positional arguments get included in the log `message`
using `str()` or `json.dumps(obj, indent=4)` in case of dicts.

Keyword arguments, other than "reserved" ones, get appended
to the logs as {key}={value}


### Reserved arguments:
* host:
  By default set to `127.0.0.1`, this argument holds the address of the codeCTRL server.

* port:
  By default set to `3001`, this is the port the codeCTRL server should be contacted at.

* surround:
  By default `3`, this argument specifies the number of lines of code that should be displayed around the call to `codectrl.log`.
