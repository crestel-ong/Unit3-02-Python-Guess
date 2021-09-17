#!/usr/bin/env python3

# Created by: Crestel Ong
# Created on: Sept 2021
# This program sees if you can guess the number its thinking of

import constants


def main():
    # this function sees if you can guess the number

    # input
    guess_number = int(input("Enter a number between 0-9: "))

    # process and output
    if guess_number == constants.RIGHT_NUMBER:
        print("You guessed correctly!")
        print("\nDone.")

    if guess_number != constants.RIGHT_NUMBER:
        print("You guessed wrong!")
        print("\nDone.")


if __name__ == "__main__":
    main()
