#!/usr/bin/python3
def print_last_digit(number):
    number = abs(number)
    
    last_digit = number % 10
    
    result = str(last_digit) + str(last_digit)

    print(result)
