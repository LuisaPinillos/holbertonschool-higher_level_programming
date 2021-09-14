#!/usr/bin/python3
separator = ', '
for j in range(0, 100):
    if (j < 10):
        print("0"'{}'", " .format(j), end='')
    if (j > 10):
        if j == 99:
            separator = '\n'
        print('{}' .format(j), end=separator)
