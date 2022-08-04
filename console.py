#!/usr/bin/python3
"""Entry point to our command interpreter"""


import cmd
import sys
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """The console of our program"""
    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """Handles the EOF character"""
        sys.exit()

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        sys.exit()

    def emptyline(self):
        """Overriding the default emptyline method"""
        pass

    def do_create(self, class_name):
        """Creates a new instance of BaseModel"""
        if class_name:
           model = map_class_name(class_name)
           if model is not None:
               new_instance = model()
               new_instance.save()
               print(new_instance.id)

           else:
               print("** class doesn't exist **")
        else:
            print("** class name missing **")

        

def map_class_name(class_name):
    """Checks if class exists"""
    if class_name == "BaseModel":
        return BaseModel
    else:
        return None


if __name__ == '__main__':
    HBNBCommand().cmdloop()
