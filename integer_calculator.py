#!/usr/bin/env python3

# Created by Marwan Mashaly
# Created on September 2019
# This program calculates the total of 2 numbers added together


def main():
    # this function calculates the total of 2 numbers added together

    # input
    integer1 = int(input("Enter integer 1: "))
    integer2 = int(input("Enter integer 2: "))

    # process
    total = integer1+integer2

    # output
    print("")
    print("{} + {} = {} ".format(integer1, integer2, total))


if __name__ == "__main__":
    main()
