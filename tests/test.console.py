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
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_empty_line(self):
        with patch("sys.stdout", new=StringIO()) as file:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", file.getvalue().strip())


class TestHBNBCommand_help(unittest.TestCase):
    """Unittests for testing help messages of the HBNB command interpreter."""

    def test_help_quit(self):
        help_out = "Quit command to exit the program."
        with patch("sys.stdout", new=StringIO()) as file:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(help_out, file.getvalue().strip())

    def test_help_create(self):
        help_out = ("Usage: create <class>\n        "
                    "Create a new class instance and print its id.")
        with patch("sys.stdout", new=StringIO()) as file:
            self.assertFalse(HBNBCommand().onecmd("help create"))
            self.assertEqual(help_out, file.getvalue().strip())

    def test_help_EOF(self):
        help_out = "EOF signal to exit the program."
        with patch("sys.stdout", new=StringIO()) as file:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertEqual(help_out, file.getvalue().strip())

    def test_help_show(self):
        help_out = ("Usage: show <class> <id> or <class>.show(<id>)\n        "
                    "Display the string representation of a class instance of"
                    " a given id.")
        with patch("sys.stdout", new=StringIO()) as file:
            self.assertFalse(HBNBCommand().onecmd("help show"))
            self.assertEqual(help_out, file.getvalue().strip())

    def test_help_destroy(self):
        h_o = ("Usage: destroy <class> <id> or <class>.destroy(<id>)\n        "
               "Delete a class instance of a given id.")
        with patch("sys.stdout", new=StringIO()) as file:
            self.assertFalse(HBNBCommand().onecmd("help destroy"))
            self.assertEqual(h_o, file.getvalue().strip())

    def test_help_all(self):
        h_o = ("Usage: all or all <class> or <class>.all()\n        "
               "Display string representations of all instances of given class"
               ".\n        If no class is specified, displays all instantiated"
               "objects.")
        with patch("sys.stdout", new=StringIO()) as file:
            self.assertFalse(HBNBCommand().onecmd("help all"))
            self.assertEqual(h_o, file.getvalue().strip())

    def test_help_count(self):
        help_out = ("Usage: count <class> or <class>.count()\n        "
                    "Retrieve the number of instances of a given class.")
        with patch("sys.stdout", new=StringIO()) as file:
            self.assertFalse(HBNBCommand().onecmd("help count"))
            self.assertEqual(help_out, file.getvalue().strip())

    def test_help_update(self):
        h_o = ("Usage: update <class> <id> <attrib_name> <attrib_value> or"
               "\n       <class>.update(<id>, <attribute_name>, <attrib_value"
               ">) or\n       <class>.update(<id>, <dictionary>)\n        "
               "Update a class inst of a given id by adding or updating\n   "
               "     a given attribute key/value pair or dictionary.")
        with patch("sys.stdout", new=StringIO()) as file:
            self.assertFalse(HBNBCommand().onecmd("help update"))
            self.assertEqual(h_o, file.getvalue().strip())

    def test_help(self):
        h_o = ("Documented commands (type help <topic>):\n"
               "========================================\n"
               "EOF  all  count  create  destroy  help  quit  show  update")
        with patch("sys.stdout", new=StringIO()) as file:
            self.assertFalse(HBNBCommand().onecmd("help"))
            self.assertEqual(h_o, file.getvalue().strip())


class TestHBNBCommand_exit(unittest.TestCase):
    """Unittests for testing exiting from the HBNB command interpreter."""

    def test_quit_exits(self):
        with patch("sys.stdout", new=StringIO()) as file:
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_EOF_exits(self):
        with patch("sys.stdout", new=StringIO()) as file:
            self.assertTrue(HBNBCommand().onecmd("EOF"))


if __name__ == "__main__":
    unittest.main()
