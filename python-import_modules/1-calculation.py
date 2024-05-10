#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
a = 10
b = 5
add_result = add(a, b)
sub_result = sub(a, b)
mul_result = mul(a, b)
div_result = div(a, b)
if __name__ == "__main__":
    print('add: {}'.format(add_result))
    print('sub: {}'.format(sub_result))
    print('mul: {}'.format(mul_result))
    print('div: {}'.format(div_result))
