import re

def process_commands(commands):
    return re.split(r'[,;\s]+', commands)

def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False