#!/usr/bin/python3
ascii_value_a = ord('a')

output = ""

for i in range(26):
    letter = chr(ascii_value_a + i)
    if letter != 'q' and letter != 'e':
        output += letter

print(output)
