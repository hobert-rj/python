from os import name as osname, system


def clearConsole():
    """Clears console page out of prevoius outputs"""
    command = 'clear'
    if osname in ('nt', 'dos'):
        command = 'cls'
    system(command)
