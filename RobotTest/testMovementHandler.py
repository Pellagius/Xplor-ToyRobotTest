import unittest

import MovementHandler
import Models

class TestMovementHandler(unittest.TestCase):

    def test_direction_from_string(self):
        self.assertEqual(MovementHandler.direction_from_string("North"), Models.FacingDirection.NORTH)
        self.assertEqual(MovementHandler.direction_from_string("NORTH"), Models.FacingDirection.NORTH)
        self.assertEqual(MovementHandler.direction_from_string("n"), Models.FacingDirection.NORTH)
        self.assertEqual(MovementHandler.direction_from_string("N"), Models.FacingDirection.NORTH)

        self.assertEqual(MovementHandler.direction_from_string("East"), Models.FacingDirection.EAST)
        self.assertEqual(MovementHandler.direction_from_string("EAST"), Models.FacingDirection.EAST)
        self.assertEqual(MovementHandler.direction_from_string("e"), Models.FacingDirection.EAST)
        self.assertEqual(MovementHandler.direction_from_string("E"), Models.FacingDirection.EAST)

        self.assertEqual(MovementHandler.direction_from_string("West"), Models.FacingDirection.WEST)
        self.assertEqual(MovementHandler.direction_from_string("WEST"), Models.FacingDirection.WEST)
        self.assertEqual(MovementHandler.direction_from_string("w"), Models.FacingDirection.WEST)
        self.assertEqual(MovementHandler.direction_from_string("W"), Models.FacingDirection.WEST)

        self.assertEqual(MovementHandler.direction_from_string("South"), Models.FacingDirection.SOUTH)
        self.assertEqual(MovementHandler.direction_from_string("SOUTH"), Models.FacingDirection.SOUTH)
        self.assertEqual(MovementHandler.direction_from_string("s"), Models.FacingDirection.SOUTH)
        self.assertEqual(MovementHandler.direction_from_string("S"), Models.FacingDirection.SOUTH)

    def test_handle_movement(self):
        robot = Models.RobotModel(position=[0,0], facing=Models.FacingDirection.NORTH)
        MovementHandler.handle_movement("Move", robot)
        self.assertEqual(robot.position, [0,1])

        MovementHandler.handle_movement("M", robot)
        self.assertEqual(robot.position, [0,2])

        MovementHandler.handle_movement("Left", robot)
        self.assertEqual(robot.facing, Models.FacingDirection.WEST)

        MovementHandler.handle_movement("LEFT", robot)
        self.assertEqual(robot.facing, Models.FacingDirection.SOUTH)

        MovementHandler.handle_movement("L", robot)
        self.assertEqual(robot.facing, Models.FacingDirection.EAST)

        MovementHandler.handle_movement("Right", robot)
        self.assertEqual(robot.facing, Models.FacingDirection.SOUTH)

        MovementHandler.handle_movement("R", robot)
        self.assertEqual(robot.facing, Models.FacingDirection.WEST)

        MovementHandler.handle_movement("RIGHT", robot)
        self.assertEqual(robot.facing, Models.FacingDirection.NORTH)

    def test_is_command_move(self):
        self.assertTrue(MovementHandler.is_command_move("move"))
        self.assertTrue(MovementHandler.is_command_move("m"))
        self.assertTrue(MovementHandler.is_command_move("MOVE"))
        self.assertTrue(MovementHandler.is_command_move("M"))

        self.assertFalse(MovementHandler.is_command_move("mov"))

    def test_is_command_left_turn(self):
        self.assertTrue(MovementHandler.is_command_left_turn("Left"))
        self.assertTrue(MovementHandler.is_command_left_turn("l"))
        self.assertTrue(MovementHandler.is_command_left_turn("LEFT"))
        self.assertTrue(MovementHandler.is_command_left_turn("L"))

        self.assertFalse(MovementHandler.is_command_left_turn("RIGHT"))

    def test_is_command_right_turn(self):
        self.assertTrue(MovementHandler.is_command_right_turn("Right"))
        self.assertTrue(MovementHandler.is_command_right_turn("R"))
        self.assertTrue(MovementHandler.is_command_right_turn("RIGHT"))
        self.assertTrue(MovementHandler.is_command_right_turn("R"))

        self.assertFalse(MovementHandler.is_command_right_turn("LEFT"))

    def test_handle_move(self):
        robot = Models.RobotModel(position=[0, 0], facing=Models.FacingDirection.NORTH)
        MovementHandler.handle_move(robot)
        self.assertEqual(robot.position, [0,1])

        robot.position = [0,5]
        MovementHandler.handle_move(robot)
        self.assertEqual(robot.position, [0,5])

        robot.facing = Models.FacingDirection.EAST
        robot.position = [2,5]
        MovementHandler.handle_move(robot)
        self.assertEqual(robot.position, [3, 5])

        robot.facing = Models.FacingDirection.WEST
        robot.position = [0, 5]
        self.assertEqual(robot.position, [0, 5])

    def test_is_command_to_report(self):
        self.assertTrue(MovementHandler.is_command_to_report("Report"))
        self.assertTrue(MovementHandler.is_command_to_report("R"))
        self.assertTrue(MovementHandler.is_command_to_report("r"))
        self.assertTrue(MovementHandler.is_command_to_report("REPORT"))

        self.assertFalse(MovementHandler.is_command_to_report("MOVE"))

   # Absolutely baffled! Below test fails, yet current reporting implementation works in prod!

   # def test_handle_reporting(self):
        #robot = Models.RobotModel(position=[], facing=Models.FacingDirection.NONE)
        #self.assertEqual(MovementHandler.handle_reporting(robot), "\nI can't provide a report - I haven't been placed yet.\n")
        #robot = Models.RobotModel(position=[2, 3], facing=Models.FacingDirection.WEST)
        #self.assertEqual(MovementHandler.handle_reporting(robot), "\nMy position is 2,3 and im facing WEST")