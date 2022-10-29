#!/usr/bin/python3
"""Entry point of the command interpreter,"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """Contains the entry point of the command interpreter."""
    prompt = '(hbnh) '
    __cls_names = {
            "BaseModel",
            "User",
            "State",
            "City",
            "Amenity",
            "Place",
            "Review"
            }

    def emptyline(self):
        """Do nothing if nothing is given."""
        pass

    def do_quit(self, arg):
        """Exits the program"""
        return True

    def do_EOF(self, arg):
        """Exits the program."""
        print("")
        return True

    def do_create(self, arg):
        """Creates an instance. of BaseModel and prints its id"""
        ags = arg.split()
        if len(ags) == 0:
            print("** class name missing **")
        elif ags[0] in HBNBCommand.__cls_names:
            print(eval(ags[0])().id)
            storage.save()
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints string rep of an instance based on the class name and id"""
        ags = arg.split()
        all_obj = storage.all()
        if len(ags) == 0:
            print("** class name missing **")
        elif ags[0] not in HBNBCommand.__cls_names:
            print("** class doesn't exist **")
        elif ags[0] in HBNBCommand.__cls_names and len(ags) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(ags[0], ags[1]) not in all_obj:
            print("** no instance found **")
        else:
            print(all_obj["{}.{}".format(ags[0], ags[1])])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        ags = arg.split()
        all_obj = storage.all()
        if len(ags) == 0:
            print("** class name missing **")
        elif ags[0] not in HBNBCommand.__cls_names:
            print("** class doesn't exist **")
        elif len(ags) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(ags[0], ags[1]) not in all_obj:
            print("** no instance found **")
        else:
            del all_obj["{}.{}".format(ags[0], ags[1])]
            storage.save()

    def do_all(self, arg):
        """Prints all str rep all instances based or not on the class name"""
        ags = arg.split()
        if len(ags) > 0 and ags[0] not in HBNBCommand.__cls_names:
            print("** class doesn't exist **")
        else:
            objs = []
            for o in storage.all().values():
                if len(ags) > 0 and (ags[0] in HBNBCommand.__cls_names):
                    objs.append(o.__str__())
                elif len(ags) == 0:
                    objs.append(o.__str__())
            print(objs)

    def do_update(self, arg):
        """Updates an instance based on the class name and id.
        Usage:
            update <class name> <id> <attribute name> "<attribute value>"
        """
        ags = arg.split()
        all_obj = storage.all()
        if len(ags) == 0:
            print("** class name missing **")
            return False
        if len(ags) > 0 and (ags[0] not in HBNBCommand.__cls_names):
            print("** class doesn't exist **")
            return False
        if len(ags) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(ags[0], ags[1]) not in all_obj:
            print("** no instance found **")
            return False
        if len(ags) == 2:
            print("** attribute name missing **")
        if len(ags) == 3:
            print("** value missing **")
        if len(ags) == 4:
            obj = all_obj["{}.{}".format(ags[0], ags[1])]
            if ags[2] in obj.__class__.__dict__.keys():
                type_arg2 = type(obj.__class__.__dict__[ags[2]])
                obj.__dict__[ags[2]] = type_arg2(ags[3])
            else:
                obj.__dict__[ags[2]] = ags[3]
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
