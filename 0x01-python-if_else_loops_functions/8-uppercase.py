#!/usr/bin/python3

def uppercase(str):
    for ch in str:
        cha = ord(ch)
        if cha >= 97 and cha <= 122:
            cha -= 32
        print("{:c}".format(cha), end="")
    print()
