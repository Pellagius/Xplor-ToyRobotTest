import Helpers
import unittest

class TestHelpers(unittest.TestCase):

    def test_process_commands_basic(self):
        self.assertEqual(
            Helpers.process_commands("run, jump; walk"),
            ["run", "jump", "walk"]
        )

    def test_process_commands_multiple_spaces(self):
        self.assertEqual(
            Helpers.process_commands("run   jump   walk"),
            ["run", "jump", "walk"]
        )

    def test_process_commands_mixed_delimiters(self):
        self.assertEqual(
            Helpers.process_commands("run,  jump;walk  stop"),
            ["run", "jump", "walk", "stop"]
        )

    def test_process_commands_leading_trailing_delimiters(self):
        self.assertEqual(
            Helpers.process_commands("  ;run, jump; "),
            ["", "run", "jump", ""]
        )
        # If you want to ignore empty strings, you'd handle that in your function.
        # But this test reflects the actual current behavior.

    def test_is_integer_valid(self):
        self.assertTrue(Helpers.is_integer("10"))
        self.assertTrue(Helpers.is_integer("-3"))
        self.assertTrue(Helpers.is_integer("0"))

    def test_is_integer_invalid(self):
        self.assertFalse(Helpers.is_integer("abc"))
        self.assertFalse(Helpers.is_integer("10.5"))
        self.assertFalse(Helpers.is_integer(""))

    def test_is_integer_with_whitespace(self):
        # int() can parse whitespace-wrapped numbers
        self.assertTrue(Helpers.is_integer("   42  "))
        self.assertFalse(Helpers.is_integer(" 42x "))