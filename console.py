#!/usr/bin/python3
"""Entry point to our command interpreter"""
import cmd
import sys
from models.base_model import BaseModel
import json
from models import storage


def parse(arg):
    l = arg.split(" ")
    if l[0]:
        return l
    return []


class HBNBCommand(cmd.Cmd):
    """The console of our program"""
    prompt = '(hbnb) '
    __models = ["BaseModel"]

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
                if len(args) >= 2 :
                    key = "{}.{}".format(args[0], args[1])
                    if key in objects:
                        print(objects[key])
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

    def do_all(slef, arg):
        """Prints all string representation of all instances
        based or not on the class name"""
        args = parse(arg)
        if len(args) > 0 and args[0] not in HBNBCommand.__models:
            print("** class doesn't exist **")
        else:
            objects_list = []
            for obj in storage.all().value():
                if len(args) > 0 and args[0] == obj.__class__.__name__:
                    objects_list.append(obj.__str__())
                elif len(args) == 0:
                    objects_list.append(obj.__str__())
            print(objects_list)




if __name__ == '__main__':
    HBNBCommand().cmdloop()
