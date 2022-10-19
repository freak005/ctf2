#!/usr/bin/env python
import os

SEED = 0

def rand():
    global SEED
    SEED = (((((SEED * 24362837402) & 0xFFFFFFFF) + 15) % 0x1000000000000) % 0xffffffff)
    return SEED


def main():
    global SEED
    SEED = int(os.getenv("SEED"))

    while True:
        i = input("> ")
        if i == "guess":
            guess = input("? ")
            if int(guess) == SEED:
                print(os.getenv("FLAG"))
        else:
            print(rand())


if __name__ == "__main__":
    main()
