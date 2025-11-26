from Models import RobotModel
import MovementHandler
import PlacementHandler
import Helpers
import Strings

robot = RobotModel
commands_list = []

def begin():
    show_prompt()
    while True:
        commands = input(Strings.command_prompt)
        handle(commands)
        continue


def show_prompt():
    print(Strings.help_prompt)

def handle(commands):
    global commands_list
    global robot
    if robot.is_placed():
        report = MovementHandler.handle_movement(Helpers.process_commands(commands), robot)
        if report:
            print(report)
        print(Strings.str_movement_complete)
    else:
        commands_list = PlacementHandler.handle_placement(Helpers.process_commands(commands))
        if commands_list:
            placement_commands = commands_list[:4]
            robot.position = [int(placement_commands[1]), int(placement_commands[2])]
            robot.facing = MovementHandler.direction_from_string(placement_commands[3])
            if commands_list[4:]:
                report = MovementHandler.handle_movement(commands_list[4:], robot)
                if report:
                    print(report)
                print(Strings.str_placement_and_movement_complete)
            else:
                print(Strings.str_placement_success)



