#!/usr/bin/python3
import sys

if __name__ != "__main__":
    exit()

args = "{:d} argument"
argsc = len(sys.argv) - 1
if argsc == 0:
    args += 's.'
elif argsc == 1:
    args += ':'
else:
    args += 's:'
print(args.format(argsc))

x = 0
for argument in sys.argv:
    if x != 0:
        print("{:d}: {:s}".format(x, argument))
    x += 1
