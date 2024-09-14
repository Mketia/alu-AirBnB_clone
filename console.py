#!/usr/bin/python3
"""Command module for the HBNB command interpreter"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.place import Place
from models.user import User
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the HBNB application"""

    prompt = "(hbnb) "
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Review": Review
    }

    def do_quit(self, arg):
        """Exit the program

        Usage:
            quit
        """
        return True

    def do_EOF(self, arg):
        """Handle EOF to exit the program

        Usage:
            EOF
        """
        print()
        return True

    def emptyline(self):
        """Do nothing on an empty line + ENTER"""
        pass

    def do_create(self, cname):
        """Create a new instance of a class, save it, and print the id

        Usage:
            create <class name>
        """
        if not cname:
            print("** class name missing **")
            return
        elif cname not in self.classes:
            print("** class doesn't exist **")
            return
        else:
            cnew = self.classes[cname]()
            cnew.save()
            print(cnew.id)

    def do_show(self, cname):
        """Print the string representation of an instance based on class name and id

        Usage:
            show <class name> <id>
        """
        args = cname.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        else:
            k = f"{args[0]}.{args[1]}"
            if k not in storage.all():
                print("** no instance found **")
                return
            print(storage.all()[k])

    def do_destroy(self, cname):
        """Delete an instance based on class name and id

        Usage:
            destroy <class name> <id>
        """
        args = cname.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        else:
            k = f"{args[0]}.{args[1]}"
            if k not in storage.all():
                print("** no instance found **")
                return
            del storage.all()[k]
            storage.save()

    def do_all(self, cname):
        """Print all string representations of all instances or of a specific class

        Usage:
            all [<class name>]
        """
        args = cname.split()
        d_list = []
        d = storage.all()
        if len(args) == 0:
            for v in d.values():
                d_list.append(str(v))
        else:
            if args[0] not in self.classes:
                print("** class doesn't exist **")
                return
            else:
                for k, v in d.items():
                    if k.startswith(args[0]):
                        d_list.append(str(v))
        print(d_list)

    def do_update(self, cname):
        """Update instance based on class name and id by adding or updating attributes

        Usage:
            update <class name> <id> <attribute name> <attribute value>
        """
        args = cname.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        k = f"{args[0]}.{args[1]}"
        if k not in storage.all():
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        clas = storage.all()[k]
        atrrname = args[2]
        atrrvalue = args[3].strip('"')
        try:
            atrrvalue = int(atrrvalue)
        except ValueError:
            try:
                atrrvalue = float(atrrvalue)
            except ValueError:
                atrrvalue = str(atrrvalue)
        setattr(clas, atrrname, atrrvalue)
        clas.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
