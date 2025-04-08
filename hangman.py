# Ryan Cannon
# SDEV 220 Final Project Part 1
# Create a hangman game
# May 15, 2022
from tkinter import *
from tkinter import messagebox

# Todo
# Create list for hangman words
# Create code for displaying house pieces for when the user enters a wrong letter
# Still need to code out house

def checkGuess(correctAnswers,guess):

    if guess == correctAnswers:
        pass
    else:
        pass


def main():
    window = Tk()
    window.mainloop()
    correctAnswers = open("hangmanAnswers.txt", "r")
    guess = input("Enter a letter: ")
    checkGuess(correctAnswers,guess)


main()


