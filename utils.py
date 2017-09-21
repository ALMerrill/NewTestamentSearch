import os

class colors:
    REVERSE = '\033[7m'
    UNDERLINE = '\033[4m'
    BOLD = '\033[1m'
    NORMAL = '\033[0m'
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    UNDERLINE = '\033[4m'
    TEST = '\x1b[0;30;47m'
    heading = '\x1b[0;37;40m'

def clear():
    os_name = os.name
    if os_name == "posix": # if OS is unix based this should work
        os.system('clear')
    elif os_name == "nt": # if OS is windows
        os.system('cls')
    else:
        pass