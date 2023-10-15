#!/usr/bin/python3
"""Define unittest for console.py"""

import unittest
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch


class TestHBNBCommand_prompting(unittest.TestCase):
    """Unittests for testing prompting of the HBNB command interpreter."""

    def test_prompt_string(self):
        """Test prompt string"""
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_empty_line(self):
        """Test empty line"""
        with patch("sys.stdout", new=StringIO()) as file:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", file.getvalue().strip())


class TestHBNBCommand_help(unittest.TestCase):
    """Unittests for testing help messages of the HBNB command interpreter."""

    def test_help_quit(self):
        """Test Quit command help text"""
        help_out = "Quit command to exit the program."
        with patch("sys.stdout", new=StringIO()) as file:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(help_out, file.getvalue().strip())

    def test_help_create(self):
        """Test create command help text"""
        help_out = "Create a new class instance and print its id."
        with patch("sys.stdout", new=StringIO()) as file:
            self.assertFalse(HBNBCommand().onecmd("help create"))
            self.assertEqual(help_out, file.getvalue().strip())

    def test_help_EOF(self):
        """Test EOF case help text"""
        help_out = "EOF signal to exit program."
        with patch("sys.stdout", new=StringIO()) as file:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertEqual(help_out, file.getvalue().strip())

    def test_help_show(self):
        """Test show command help text"""
        help_out = """Display the string representation of a class instance
        of a given id."""

        with patch("sys.stdout", new=StringIO()) as file:
            self.assertFalse(HBNBCommand().onecmd("help show"))
            self.assertEqual(help_out, file.getvalue().strip())

    def test_help_destroy(self):
        """Test destroy command help text"""
        h_o = "Delete a class instance of a given id."
        with patch("sys.stdout", new=StringIO()) as file:
            self.assertFalse(HBNBCommand().onecmd("help destroy"))
            self.assertEqual(h_o, file.getvalue().strip())

    def test_help_all(self):
        """Test all command help text"""
        h_o = "Display string representations of all instances of given class."
        with patch("sys.stdout", new=StringIO()) as file:
            self.assertFalse(HBNBCommand().onecmd("help all"))
            self.assertEqual(h_o, file.getvalue().strip())

    def test_help_count(self):
        """Test count command help text"""
        help_out = "*** No help on count"
        with patch("sys.stdout", new=StringIO()) as file:
            self.assertFalse(HBNBCommand().onecmd("help count"))
            self.assertEqual(help_out, file.getvalue().strip())

    def test_help_update(self):
        """Test update command help text"""
        h_o = """Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary."""

        with patch("sys.stdout", new=StringIO()) as file:
            self.assertFalse(HBNBCommand().onecmd("help update"))
            self.assertEqual(h_o, file.getvalue().strip())

    def test_help(self):
        """ test help command output"""
        h_o = ("Documented commands (type help <topic>):\n"
               "========================================\n"
               "EOF  all  create  destroy  help  quit  show  update")

        with patch("sys.stdout", new=StringIO()) as file:
            self.assertFalse(HBNBCommand().onecmd("help"))
            self.assertEqual(h_o, file.getvalue().strip())


class TestHBNBCommand_exit(unittest.TestCase):
    """Unittests for testing exiting from the HBNB command interpreter."""

    def test_quit_exits(self):
        """Test if quit command exits the console"""
        with patch("sys.stdout", new=StringIO()) as file:
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_EOF_exits(self):
        """Test if EOF condition exits the console"""
        with patch("sys.stdout", new=StringIO()) as file:
            self.assertTrue(HBNBCommand().onecmd("EOF"))


if __name__ == "__main__":
    unittest.main()
