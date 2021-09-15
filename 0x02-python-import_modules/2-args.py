#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    lengarvs = len(argv) - 1
    j = 1
    if lengarvs == 1:
        print("{} argument:" .format(lengarvs))
        print("{}: {} " .format(lengarvs, argv[1]))
    elif lengarvs == 0:
        print("0 arguments." .format(lengarvs))
    else:
        print("{} arguments:" .format(lengarvs))
        for j in range(1, lengarvs + 1):
            print("{}: {}" .format(j, argv[j]))
