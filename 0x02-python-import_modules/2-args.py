#!/usr/bin/python3
import sys

args = sys.argv[1:]
num_args = len(args)

print("Number of argument{}: {}".format("s" if num_args > 1 else "",
num_args), end="")
if num_args == 0:
    print(".")
else:
    print(":")
    for i, arg in enumerate(args):
        print("{}: {}".format(i+1, arg))
