import unittest

import PlacementHandler
import Models

class TestPlacementHandler(unittest.TestCase):

    def test_handle_placement(self):
        commands_list = ["place", "2", "3", "S"]
        self.assertEqual(PlacementHandler.handle_placement(commands_list), ["place", "2", "3", "S"])

    def test_find_last_placement_command(self):
        commands_list = ["move", "l", "m"]
        self.assertEqual(PlacementHandler.find_last_placement_command(commands_list), [])
        commands_list = ["move", "left", "place", "2", "3", "S"]
        self.assertEqual(PlacementHandler.find_last_placement_command(commands_list), ["place", "2", "3", "S"])
        commands_list = ["place", "2", "3", "S", "place", "0", "0", "north"]
        self.assertEqual(PlacementHandler.find_last_placement_command(commands_list), ["place", "0", "0", "north"])

    def test_is_valid_position(self):
        commands_list = ["1","2"]
        self.assertTrue(PlacementHandler.is_valid_position(commands_list))
        commands_list = ["a", "b"]
        self.assertFalse(PlacementHandler.is_valid_position(commands_list))

        commands_list = ["2", "/3"]
        self.assertFalse(PlacementHandler.is_valid_position(commands_list))

    def test_is_valid_facing(self):
        command = "North"
        self.assertTrue(PlacementHandler.is_valid_facing(command))
        command = "South"
        self.assertTrue(PlacementHandler.is_valid_facing(command))
        command = "West"
        self.assertTrue(PlacementHandler.is_valid_facing(command))
        command = "East"
        self.assertTrue(PlacementHandler.is_valid_facing(command))

        command = "Down"
        self.assertFalse(PlacementHandler.is_valid_facing(command))