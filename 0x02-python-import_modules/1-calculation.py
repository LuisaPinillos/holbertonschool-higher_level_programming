#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import *

    a = 10
    b = 5
    suma = add(a, b)
    resta = sub(a, b)
    Mul = mul(a, b)
    Div = div(a, b)
    print("{} + {} = {}" .format(a, b, suma))
    print("{} - {} = {}" .format(a, b, resta))
    print("{} * {} = {}" .format(a, b, Mul))
    print("{} / {} = {}" .format(a, b, Div))
