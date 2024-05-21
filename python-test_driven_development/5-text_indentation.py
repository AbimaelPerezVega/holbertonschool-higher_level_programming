#!/usr/bin/python3
"""
This module provides a function to
print a text with 2 new lines after each
of these characters: ., ? and :.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :.

    Parameters:
    text (str): The input text to be processed.

    Raises:
    TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    special_chars = {'.', '?', ':'}
    new_text = ""
    i = 0

    while i < len(text):
        new_text += text[i]
        if text[i] in special_chars:
            new_text += "\n\n"
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1

    print(new_text, end="")
