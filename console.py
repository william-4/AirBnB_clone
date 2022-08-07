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


def parse(arg):
    lists = arg.split(" ")
    if lists[0]:
        return lists
    return []


class HBNBCommand(cmd.Cmd):
    """The console of our program"""
    prompt = '(hbnb) '
    __models = ["BaseModel", "User",
                "Place", "State", "City",
                "Amenity", "Review"]

    def do_EOF(self, arg):
        """Handles the EOF character"""
        print()
        quit()

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        quit()

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
                                # objects[key].args[2] = args[3]
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
