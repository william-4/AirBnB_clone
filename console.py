#!/usr/bin/python3
"""Entry point to our command interpreter"""
import cmd
import sys
from models.base_model import BaseModel
import json
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from shlex import split
import re


def parse(arg):
    curly_braces = re.search(r'\{(.*?)\}', arg)
    brackets = re.search(r'\[(.*?)\]', arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            args = [i.strip(",") for i in split(arg[:brackets.span()[0]])]
            args.append(brackets.group())
            return args
    else:
        args = [i.strip(",") for i in split(arg[:curly_braces.span()[0]])]
        args.append(curly_braces.group())
        return args


class HBNBCommand(cmd.Cmd):
    """The console of our program"""
    prompt = '(hbnb) '
    __models = ["BaseModel", "User",
                "Place", "State", "City",
                "Amenity", "Review"]

    def default(self, arg):
        """Defines the default behaviour when the command is invalid"""
        commands = {
                "all": self.do_all,
                "count": self.count,
                "show": self.do_show,
                "destroy": self.do_destroy,
                "update": self.do_update
        }
        dot_usage = re.search(r'\.', arg)
        if dot_usage is not None:
            args = [arg[:dot_usage.span()[0]], arg[dot_usage.span()[1]:]]
            brackets = re.search(r'\((.*?)\)', args[1])
            if brackets is not None:
                command = [args[1][:brackets.span()[0]], brackets.group()[1:-1]]
                if command[0] in commands.keys():
                    arguments = "{} {}".format(args[0], command[1])
                    return commands[command[0]](arguments)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_EOF(self, arg):
        """Handles the EOF character"""
        print()
        return True

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def emptyline(self):
        """Overriding the default emptyline method"""
        return

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        args = parse(arg)
        if len(args) >= 1:
            if args[0] in HBNBCommand.__models:
                print(eval(args[0])().id)
                storage.save()
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id"""
        args = parse(arg)
        objects = storage.all()
        if len(args) >= 1:
            if args[0] in HBNBCommand.__models:
                if len(args) >= 2:
                    key = "{}.{}".format(args[0], args[1])
                    if key in objects:
                        print(objects[key])
                        storage.save()
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = parse(arg)
        objects = storage.all()
        if len(args) >= 1:
            if args[0] in HBNBCommand.__models:
                if len(args) >= 2:
                    key = "{}.{}".format(args[0], args[1])
                    if key in objects:
                        del objects[key]
                        storage.save()
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class name"""
        args = parse(arg)
        if len(args) > 0 and args[0] not in HBNBCommand.__models:
            print("** class doesn't exist **")
        else:
            objects_list = []
            for obj in storage.all().values():
                if len(args) > 0 and args[0] == type(obj).__name__:
                    objects_list.append(str(obj))
                elif len(args) == 0:
                    objects_list.append(str(obj))
            print(objects_list)

    def count(self, arg):
        """A function that counts instances of a model"""
        args = parse(arg)
        if len(args) > 0 and args[0] not in HBNBCommand.__models:
            print("** class doesn't exist **")
        else:
            objects_list = []
            for obj in storage.all().values():
                if len(args) > 0 and args[0] == type(obj).__name__:
                    objects_list.append(str(obj))
                elif len(args) == 0:
                    objects_list.append(str(obj))
            print(len(objects_list))

    def do_update(self, arg):
        """Updates an instance based on the class name and id
        by adding or updating attribute"""
        args = parse(arg)
        objects = storage.all()
        if len(args) > 0:
            if args[0] in HBNBCommand.__models:
                if len(args) >= 2:
                    key = "{}.{}".format(args[0], args[1])
                    if key in objects:
                        if len(args) >= 3:
                            if len(args) == 4:
                                setattr(objects[key], args[2], str(args[3]))
                                storage.save()
                            elif type(eval(args[2])) is dict:
                                for k, v in eval(args[2]).items():
                                    setattr(objects[key], k, v)
                                storage.save()
                            else:
                                print("** value missing **")
                        else:
                            print("** attribute name missing **")
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
