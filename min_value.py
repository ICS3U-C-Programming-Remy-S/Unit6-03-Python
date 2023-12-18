#!/usr/bin/env python3
# Created by: Remy Skelton
# Created on: Dec 17, 2023
# This program will find the min of
# 10 numbers

import random
import constants


def find_min_value(list_of_int):
    # Initialize counter
    counter = 1

    # Initialize min_value to cell 0 in the list
    min_value = list_of_int[0]

    # Loop through the list to find the min value
    while counter < constants.MAX_ARRAY_SIZE:
        # find min
        if list_of_int[counter] < min_value:
            min_value = list_of_int[counter]

        # increment
        counter += counter
    return min_value


def main():
    # create list and min value
    list_of_int = []
    min_value = 0

    # Generate random numbers and fill the list
    for counter1 in range(constants.MAX_ARRAY_SIZE):
        random_num = random.randint(constants.MIN_NUM, constants.MAX_NUM)

        list_of_int.append(random_num)

        # display added numbers
        print(f"{list_of_int[counter1]} added to list")

    # call find_min_value function
    min_value = find_min_value(list_of_int)

    # display min value
    print("\nMin Value is:", min_value)


if __name__ == "__main__":
    main()
