#!/usr/bin/python3
import sys

if __name__ != "__main__":
    exit()

i = 0
results = 0
for argument in sys.argv:
    if i != 0:
        results += int(argument)
    else:
        i += 1
print("{:d}".format(results))
