#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    leng = 0
    while leng < x:
        try:
            print("{}".format(my_list[leng]), end="")
            leng += 1
        except IndexError:
            break
    print("")
    return leng
