import Models
import Strings

def direction_from_string(direction_string):
    if direction_string.lower() in ["north", "n"]:
        return Models.FacingDirection.NORTH
    elif direction_string.lower() in ["south", "s"]:
        return Models.FacingDirection.SOUTH
    elif direction_string.lower() in ["east", "e"]:
        return Models.FacingDirection.EAST
    elif direction_string.lower() in ["west", "w"]:
        return Models.FacingDirection.WEST
    else: return Models.FacingDirection.NONE


def handle_movement(movements_list, robot):
    for command in movements_list:
        if is_command_move(command):
            handle_move(robot)
        elif is_command_left_turn(command):
            handle_left_turn(robot)
        elif is_command_right_turn(command):
            handle_right_turn(robot)
        elif is_command_to_report(command):
            return handle_reporting(robot)

def is_command_move(command):
    return command.lower() in ["move", "m"]

def is_command_left_turn(command):
    return command.lower() in ["left", "l"]

def is_command_right_turn(command):
    return command.lower() in ["right", "r"]

def handle_move(robot):
    if robot.facing == Models.FacingDirection.NORTH and int(robot.position[1]) <= 4:
        robot.position[1] += 1
    elif robot.facing == Models.FacingDirection.SOUTH and int(robot.position[1]) >= 1:
        robot.position[1] -= 1
    elif robot.facing == Models.FacingDirection.EAST and int(robot.position[0]) <= 4:
        robot.position[0] += 1
    elif robot.facing == Models.FacingDirection.WEST and int(robot.position[0]) >= 1:
        robot.position[0] -= 1

def handle_left_turn(robot):
    if robot.facing == Models.FacingDirection.NORTH:
        robot.facing = Models.FacingDirection.WEST
    elif robot.facing == Models.FacingDirection.SOUTH:
        robot.facing = Models.FacingDirection.EAST
    elif robot.facing == Models.FacingDirection.EAST:
        robot.facing = Models.FacingDirection.NORTH
    elif robot.facing == Models.FacingDirection.WEST:
        robot.facing = Models.FacingDirection.SOUTH

def handle_right_turn(robot):
    if robot.facing == Models.FacingDirection.NORTH:
        robot.facing = Models.FacingDirection.EAST
    elif robot.facing == Models.FacingDirection.SOUTH:
        robot.facing = Models.FacingDirection.WEST
    elif robot.facing == Models.FacingDirection.EAST:
        robot.facing = Models.FacingDirection.SOUTH
    elif robot.facing == Models.FacingDirection.WEST:
        robot.facing = Models.FacingDirection.NORTH

def is_command_to_report(command):
    return command.lower() in ["report", "r"]

def handle_reporting(robot):
    report = robot.report()
    if report:
       return Strings.str_report.substitute(report)
    else:
        return Strings.str_not_placed