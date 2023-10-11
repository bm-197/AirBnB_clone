#!/usr/bin/python3
"""Defines the HBnB console."""

import cmd
from models import storage
from models.base_model import BaseModel

def convert(line):
    line_2 = []
    if len(line) != 0:
        line_2 = line.split(" ")
    return line_2

class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter."""

    prompt = "(hbnb)"
    __classes = {"BaseModel"}

    def do_quit(self, line):
        """Quit command to exit the progrma."""
        return True

    def do_EOF(self, line):
        """EOF signal to exit program."""
        print("")
        return True
    
    def do_create(self, line):
        """Create a new class instance and print its id."""
        line_2 = convert(line)

        if len(line_2) == 0:
            print("** class name missing **")
        
        elif line_2[0] not in HBNBCommand.__classes:
            print("** class doesn't exit **")
        
        else:
            print(eval(line_2[0])().id)
            storage.save()
    
    def do_show(self, line):
        """Display the string representation of a class instance of a given id."""
        line_2 = convert(line)
        obj = storage.all()

        if len(line_2) == 0:
            print("** class name missing **")
        
        elif line_2[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        
        elif len(line_2) == 1:
            print("** instance id missing **")

        elif "{}.{}".format(line_2[0], line_2[1]) not in obj.keys():
            print("** no instance found **")

        else:
            print(obj["{}.{}".format(line_2[0], line_2[1])])
    
    def do_destroy(self, line):
        """Delete a class instance of a given id."""
        line_2 = convert(line)
        obj = storage.all()

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
            storage.save()
    
    def do_all(self, line):
        """Display string representations of all instances of a given class."""
        line_2 = convert(line)
        objl = []
        if len(line_2) > 0 and line_2[0] not in HBNBCommand.__classes:
            print("** class doesn't exits **")
        else:
            for ob in storage.all().values():
                if len(line_2) > 0 and argl[0] == obj.__class__.__name__:
                    objl.append(ob.__str__())
                elif len(line_2) == 0:
                    objl.append(ob.__str__())
        if len(objl) != 0:
            print(objl)
        
    def do_update(self, line):
        """Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary."""
        line_2 = convert(line)
        obj = storage.all()

        if len(line_2) == 0:
            print("** class name missing **")
            return False
        
        if line_2[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        
        if len(line_2) == 1:
            print("** instance id missing **")
            return False

        """if  "{}.{}".format(line_2[0], line_2[1]) not in obj.keys():
            print("** no instance found **")
            return False"""
        
        if len(line_2) == 2:
            print("** attribute name missing **")
            return False
        
        if len(line_2) == 3:
            try:
                type(eval(len_2[2])) != dict
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

        storage.save()
                    
                    


if __name__ == '__main__':
    HBNBCommand().cmdloop()