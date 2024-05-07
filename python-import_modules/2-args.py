#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    num_args = len(argv) - 1
    if num_args == 0:
        print("0 argument.")
    elif num_args == 1:
        print("1 argument :")
    else:
        print("{} arguments :".format(num_args))

    for i in range(num_args):
        print("{}: {}".format(i + 1, argv[i + 1]))
