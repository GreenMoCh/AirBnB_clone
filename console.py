#!/usr/bin/python3
"""HBnB console"""
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.review import Review
from models.place import Place


def parse(arg):
    cb = re.search(r"\{(.*?)\}", arg)
    br = re.search(r"\[(.*?)\]", arg)
    if cb is None:
        if br is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:br.span()[0]])
            rl = [i.strip(",") for i in lexer]
            rl.append(br.group())
            return (rl)
    else:
        lexer = split(arg[:cb.span()[0]])
        rl = [i.strip(",") for i in lexer]
        rl.append(cb.group())
        return (rl)


class HBNBCommand(cmd.Cmd):
    """HolbertonBnB interpreter

    Attributes:
        prompt (str): comand prompt
    """

    prompt = "(hbnb) "
    __classes = {
            "BaseModel",
            "User",
            "State",
            "City",
            "Place",
            "Amenity",
            "Review"
            }

    def emtyline(self):
        """an empty line"""
        pass

    def default(self, arg):
        """Default cmd module"""
        argdict = {
                "all": self.do_all,
                "show": self.do_show,
                "destroy": self.do_destroy,
                "count": self.do_count,
                "update": self.do_update
                }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".fromat(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF to exit program"""
        print("")
        return True

    def do_create(self, arg):
        """Creat a new class"""
        argl = parse(arg)
        if len(argl) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist**")
        else:
            print(eval(argl[0])().id)
            storage.save()

    def do_show(self, arg):
        """displays the str of a class"""
        argl = parse(arg)
        data = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in data:
            print("**no instance found **")
        else:
            print(data["{}.{}".format(argl[0], argl[1])])

    def do_destroy(self, arg):
        """Delete a class"""
        argl = parse(arg)
        data = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommad.__classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in data.keys():
            print("** no instance found **")
        else:
            del data["{}.{}".format(argl[0], argl[1])]
            storage.save()

    def do_all(self, arg):
        """Dispalys str of all classes"""
        argl = parse(arg)
        if len(argl) > 0 and argl[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            objl = []
            for obj in storge.all().values():
                if len(argl) > 0 and argl[0] == obj.__class_.__name__:
                    objl.append(obj.__str__())
                elif len(argl) == 0:
                    objl.append(obj.__str__())
            print(objl)

    def do_count(self, arg):
        """Retrieve class"""
        argl = parse(arg)
        count = 0
        for obj in storage.all().values():
            if argl[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def do_update(self, arg):
        """Update a class"""
        argl = parse(arg)
        data = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
            return False
        if argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(argl) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(argl[0], argl[1]) not in data.keys():
            print("** no instance found **")
            return False
        if len(argl) == 2:
            print("** attribute name missing **")
            return False
        if len(argl) == 3:
            try:
                type(eval(argl[2])) != dict
            except NameError:
                print("** value missing **")
                return False
        if len(argl) == 4:
            obj = data["{}.{}".format(argl[0], argl[1])]
            if argl[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[argl[2]])
                obj.__dict__[argl[2]] = valtype(argl[3])
            else:
                obj.__dict__[argl[2]] = argl[3]
        elif type(eval(argl[2])) == dict:
            obj = data["{}.{}".format(argl[0], argl[1])]
            for k, v in eval(argl[2]).items():
                if (k in obj.__class__.__dict__.keys() and type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
