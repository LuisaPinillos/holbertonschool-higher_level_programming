#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    j = 1
    lengarvs = len(argv) - 1
    sum = 0
    for j in range(1, lengarvs + 1):
        number = int(argv[j])
        sum += number
    print("{}" .format(sum))
