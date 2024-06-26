#!/usr/bin/python3
"""function that prints a text with 2 new lines after each of
these characters: ., ? and :
arg: text must be a string
raise: typeError: must be a string
"""


def text_indentation(text):
    """function that prints a text with 2
    new lines after each of these characters: ., ? and :"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    markers = {'.', '?', ':'}
    result = ""
    i = 0
    while i < len(text):
        result += text[i]
        if text[i] in markers:
            result += "\n\n"
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1

    print(result, end="")
