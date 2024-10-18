import sys
from core.commands import Command

def command_executor():
    argv = sys.argv
    if len(argv) < 2:
        return
    cmd = Command(argv)
    cmd.execute()