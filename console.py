#!/usr/bin/python3
"""command module """

import cmd
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """Command interpreter"""

    prompt ="hbnb"
    classes = {'BaseModel': BaseModel}

    def do_quit(self, arg):
        """command to exit the program"""
        return True
    
    def do_EOF(self,arg):
        """handles EOF to exit the program"""
        print()
        return True
    
    def emptyline(self):
        """Doesn't do anything on an empty line + ENTER """
        pass

    def do_create(self,cname):
        """Creates a new instance of a class, saves it, and prints the id"""
        if len(cname) == 0:
            print("** class name missing **")
            return
        elif cname not in self.classes:
            print("** class doesn't exist **")
            return
        else:
            cnew = self.classes[cname]
            cnew.save()
            print(cnew.id)
    
    def do_show(self,cname):
        """Prints the string representation of an instance based on the class name and id"""
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

        



if __name__ == "__main__":
    HBNBCommand().cmdloop()
