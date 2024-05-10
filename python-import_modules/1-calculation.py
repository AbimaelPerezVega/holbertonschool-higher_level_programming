#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
a = 10
b = 5
add_result = add(a, b)
sub_result = sub(a, b)
mul_result = mul(a, b)
div_result = div(a, b)
if __name__ == "__main__":
    print('10 + 5 = {}'.format(add_result))
    print('10 - 5 = {}'.format(sub_result))
    print('10 * 5 = {}'.format(mul_result))
    print('10 / 5 = {}'.format(div_result))
