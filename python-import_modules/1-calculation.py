#!/usr/bin/python3
from calculator_1 import add, subtract, multiply, divide

a = 10
b = 5
add_result = add(a, b)
sub_result = subtract(a, b)
mul_result = multiply(a, b)
div_result = divide(a, b)

print("Addition:", add_result)
print("Subtraction:", sub_result)
print("Multiplication:", mul_result)
print("Division:", div_result)
