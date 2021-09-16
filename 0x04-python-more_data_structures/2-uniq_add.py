#!/usr/bin/python3
def uniq_add(my_list=[]):
    listset = list(set(my_list))
    sum = 0
    for i in range(len(listset)):
        sum += listset[i]
    return sum
