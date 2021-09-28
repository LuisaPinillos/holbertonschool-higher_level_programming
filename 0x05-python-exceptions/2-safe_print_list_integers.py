#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    leng = 0
    count = 0
    while leng < x:
        try:
            print("{:d}".format(my_list[leng]), end="")
            count += 1
            leng += 1
        except (TypeError, ValueError):
            leng += 1
    print("")
    return count
