#!/usr/bin/env python

import random 

def main():
    """Let's start guessing elements of periodic table game."""
    print("Guess the elements !")

    periodic = [
        "hydrogen",
        "helium",
        "lithium",
        "beryllium",
        "boron",
        "carbon",
        "nitrogen",
        "oxygen",
        "fluorine",
        "neon",
        "sodium",
    ]

    x = random.choice(periodic)
    print(x)
    guess = None

    while x != guess:

        guess = str(input("what elements am i thinking of? "))

        if x == guess:
            print("You guessed {}. congratulation you got it right!".format(guess))       
        else:
            print("You guessed {}. It's wrong,try again!".format(guess)) 

main()