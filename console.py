#!/usr/bin/python3
"""Defines the HBnB console."""

import cmd
import ast
import re
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def convert(line):
    """Split input from tty in with whitespace as a delimiter
        Args:
            line - tty input stream"""
    if len(line) == 0:
        return []
    line_2 = line.split(" " )
    return line_2


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter."""

    prompt = "(hbnb) "
    __classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Place": Place,
        "Amenity": Amenity,
        "Review": Review}

    def do_quit(self, line):
        """Quit command to exit the progrma."""
        return True

    def do_EOF(self, line):
        """EOF signal to exit program."""
        print("")
        return True

    def emptyline(self):
        """Do nothing if no commnd is provided"""
        return

    def do_create(self, line):
        """Create a new class instance and print its id."""
        line_2 = convert(line)

        if len(line_2) == 0:
            print("** class name missing **")

        elif line_2[0] not in self.__classes:
            print("** class doesn't exit **")

        print(self.__classes[line_2[0]]().id)
        models.storage.save()

    def do_show(self, line):
        """Display the string representation of a class instance
            of a given id."""
        line_2 = convert(line)
        line_2[-1] = line_2[-1].strip('"')
        obj = models.storage.all()

        if len(line_2) == 0:
            print("** class name missing **")
            return

        elif line_2[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return

        elif len(line_2) == 1:
            print("** instance id missing **")
            return

        elif "{}.{}".format(line_2[0], line_2[1]) not in obj.keys():
            print("** no instance found **")
            return
        print(obj["{}.{}".format(line_2[0], line_2[1])])

    def do_destroy(self, line):
        """Delete a class instance of a given id."""
        line_2 = convert(line)
        line_2[-1] = line_2[-1].strip('"')
        obj = models.storage.all()

        if len(line_2) == 0:
            print("** class name missing **")
            return

        elif line_2[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")

        elif len(line_2) == 1:
            print("** instance id missing **")

        elif "{}.{}".format(line_2[0], line_2[1]) not in obj.keys():
            print("** no instance found **")

        else:
            del obj["{}.{}".format(line_2[0], line_2[1])]
            models.storage.save()

    def do_all(self, line):
        """Display string representations of all instances of given class."""
        line_2 = convert(line) if len(line) > 0 else None
        objl = []
        if line_2 is None:
            print("** class name missing **")
        elif line_2[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            for ob in models.storage.all().values():
                if line_2[0] == ob.__class__.__name__:
                    objl.append(ob.__str__())
                elif len(line_2) == 0:
                    objl.append(ob.__str__())
        if len(objl) != 0:
            print(objl)

    def do_update(self, line):
        """Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary."""
        line_2 = convert(line)
        index = 0
        if len(line_2 ) >= 4 and line_2[3].startswith('"'):
            for arg in line_2:
                if arg.endswith('"'):
                    index = line_2.index(arg)
            if len(line_2) > index:
                line_2[3] = " ".join(line_2[3:index + 1])
            
        obj = models.storage.all()

        if len(line_2) == 0:
            print("** class name missing **")
            return False

        if line_2[0] not in self.__classes:
            print("** class doesn't exist **")
            return False

        if len(line_2) == 1:
            print("** instance id missing **")
            return False

        if "{}.{}".format(line_2[0], line_2[1]) not in obj.keys():
            print("** no instance found **")
            return False

        if len(line_2) == 2:
            print("** attribute name missing **")
            return False

        if len(line_2) == 3:
            try:
                type(eval(line_2[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(line_2) >= 4:
            line_2[3] = line_2[3].strip('"')
            ob = obj["{}.{}".format(line_2[0], line_2[1])]
            if line[2] in ob.__class__.__dict__.keys():
                value_type = type(ob.__class__.__dict__[line_2[2]])
                ob.__dict__[line_2[2]] = value_type(line_2[3])
            else:
                ob.__dict__[line_2[2]] = line_2[3]

        models.storage.save()

    def default(self, line):
        line_split = line.split(".", maxsplit=1)

        if len(line_split) != 2:
            super().default(line)
            return

        class_name, command = line_split
        match = re.search(r"\((.*?)\)", command)

        if match:
            command = [command[:match.span()[0]], match.group()[1: -1]]
            if hasattr(self, 'do_' + command[0]):
                method = getattr(self, 'do_' + command[0])
                call = class_name
                if command[0] == "update":
                    print("ahhhhhhh")
                    id_dict = command[1].split(", ", maxsplit=1)
                    if (len(id_dict) > 1 and id_dict[1][0] == "{"):
                        inst_id, dict = id_dict
                        inst_id = inst_id.strip('"')
                        dict = dict.strip('"')
                        dict = ast.literal_eval(dict)
                        for key, value in dict.items():
                            args =  inst_id + " " + key + " " + value
                            method(f"{call} {args}")
                        return
                    else:
                        args = ""
                        args = ''.join(char for char in command[1] if char not in [',', '"'])
                        if args != command[1]:
                            print(args)
                            call = f"{call} {args}"
                            method(call)
                        else:
                            method(call)
                    return

                if len(command[1]) != 0:
                    command[1] = command[1].strip('"')
                    call = f"{call} {command[1]}"
                method(call)

            elif command[0] == "count" and class_name in self.__classes:
                count = 0
                for obj in models.storage.all().values():
                    if obj.__class__.__name__ == class_name:
                        count += 1
                print(count)
        else:
            super().default(line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
