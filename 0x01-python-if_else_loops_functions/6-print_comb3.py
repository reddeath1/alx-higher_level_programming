#!/usr/bin/python3
for x in range(0, 9):
    for v in range(x + 1, 10):
        if x == 8:
            print("{:d}{:d}".format(x, v))
            break
        print("{:d}{:d}".format(x, v), end=", ")
