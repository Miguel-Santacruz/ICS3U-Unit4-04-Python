#!/usr/bin/env python3

# Created by: Miguel Santacruz
# Created on: Apr 2022
# This program is a number guessing game

import random


def main():
    # This function checks the number
    while True:
        random_number = random.randint(1, 9)

        # input
        string = input("Enter number between 0 - 9: ")

        # process & output
        try:
            decimal = float(string)
            try:
                number = int(string)
                if number < 0:
                    print("{} is not positive. Try again.".format(number))
                    print("")
                elif number > 9:
                    print("{} is out of range. Try again.".format(number))
                    print("")
                elif number == random_number:
                    print("You guessed right!")
                    break
                else:
                    print(
                        "You guessed wrong, the correct number was {}. Try again.".format(
                            random_number
                        )
                    )
                    print("")
            except Exception:
                print("{} is not an integer. Try again.".format(decimal))
                print("")
        except Exception:
            print("{} is not a number. Try again.".format(string))
            print("")

    print("\nDone.")


if __name__ == "__main__":
    main()
