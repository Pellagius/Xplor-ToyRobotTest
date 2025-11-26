import Helpers
import Strings
from Helpers import is_integer


def handle_placement(commands_list):
    commands_list = find_last_placement_command(commands_list)
    if commands_list:
        return commands_list
    else:
        return []

def find_last_placement_command(commands_list):
        for i in range(len(commands_list) - 1, -1, -1):
            if commands_list[i].lower() in ["place", "p"]:
                commands_list = commands_list[i:]
                if not is_valid_position([commands_list[1], commands_list[2]]):
                    print(Strings.str_invalid_position)
                    return []
                elif not is_valid_facing(commands_list[3]):
                    print(Strings.str_invalid_facing)
                    return []
                else:
                    return commands_list
        return []

def is_valid_position(position):
    for coordinate in position:
        if not is_integer(coordinate): return False
        elif int(coordinate) < 0 or int(coordinate) > 5:
            return False
    return True

def is_valid_facing(direction):
    return direction.lower() in ["north", "south", "east", "west", "n", "s", "w", "e"]