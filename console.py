#!/usr/bin/python3
"""Defines the HBnB console."""

import cmd
import models
from models.base_model import BaseModel

def convert(line):
    """Split input from tty in with whitespace as a delimiter
        Args:
            line - tty input stream"""
    if len(line) == 0:
        return []
    line_2 = line.split(" ")
    return line_2

class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter."""

    prompt = "(hbnb) "
    __classes = {"BaseModel": BaseModel}

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
        """Display the string representation of a class instance of a given id."""
        line_2 = convert(line)
        obj = models.storage.all()

        if len(line_2) == 0:
            print("** class name missing **")
            return
        
        elif line_2[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        
        elif len(line_2) == 1:
            print("** instance id missing **")
            return

        elif "{}.{}".format(line_2[0], line_2[1]) not in obj.keys():
            print("** no instance found **")
        print(obj["{}.{}".format(line_2[0], line_2[1])])
    
    def do_destroy(self, line):
        """Delete a class instance of a given id."""
        line_2 = convert(line)
        obj = models.storage.all()

        if len(line_2) == 0:
            print("** class name missing **")
        
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
        """Display string representations of all instances of a given class."""
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

        if  "{}.{}".format(line_2[0], line_2[1]) not in obj.keys():
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
        
        if len(line_2) == 4:
            ob = obj["{}.{}".format(line_2[0], line_2[1])]
            if line[2] in ob.__class__.__dict__.keys():
                value_type = type(ob.__class__.__dict__[line_2[2]])
                ob.__dict__[line_2[2]] = value_type(line_2[3])
            else:
                ob.__dict__[line_2[2]] = line_2[3]

        models.storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()