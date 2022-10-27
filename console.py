#!/usr/bin/python3
"""Entry point of the command interpreter,"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Contains the entry point of the command interpreter."""
    prompt = '(hbnh) '

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
