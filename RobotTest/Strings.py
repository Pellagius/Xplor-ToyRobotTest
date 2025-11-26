from string import Template

command_prompt = "Enter commands: "

help_prompt = ("\nRobot standing by!\n\n"
          "First, put me down on the table with a PLACE command followed X,Y,F, see this example:\n\n"
          "     Place 2,3,North\n\n"
          "with X and Y being 0 or greater and 5 or less - and F being NORTH, SOUTH, EAST or WEST to point me in a direction.\n"
          "After placement, you may command me with MOVE (to move forward 1 space) or LEFT or RIGHT (to turn left or right) "
          "or REPORT to show my position and current facing.\n")

str_placement_failed = "You need to PLACE me on the table with  X,Y,F coordinate first - type HELP to show instructions."

str_placement_success = "\nPlacement complete - ready to move out.\n"

str_invalid_position = ("\nWhoops! Thats not a valid position. Here is an example of how the placement should be entered:\n"
                        "X,Y,F: 2,3,North or 4,5 E or 0,0,WEST - remember, X and Y must be "
                        "between 0 and 5 inclusively - try placement again\n")

str_invalid_facing = ("\nI can only move in 4 directions - North(N), South(S), East(E), West(W),\n"
                      "the 'F' coordinate needs to be one of these - try placement again\n")

str_not_placed = "\nI can't provide a report - I haven't been placed yet.\n"

str_movement_complete = "Movements complete\n"

str_placement_and_movement_complete = "Placement done and movements complete\n"

str_report = Template('\nMy position is $x, $y and im facing $f\n')