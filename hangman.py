# task from: http://hack.engeto.com/hangman

from random import randrange
import sys
def hangman_without_graphics(wTF):
    hangmanAsciiGraphics = [
        '\n  ______\n  |   \|\n       |\n       |\n       |\n       |\n=========\n',
        '\n  ______\n  |   \|\n  O    |\n       |\n       |\n       |\n=========\n',
        '\n  ______\n  |   \|\n  O    |\n  |    |\n       |\n       |\n=========\n',
        '\n  ______\n  |   \|\n  O    |\n /|    |\n       |\n       |\n=========\n',
        '\n  ______\n  |   \|\n  O    |\n /|\   |\n       |\n       |\n=========\n',
        '\n  ______\n  |   \|\n  O    |\n /|\   |\n /     |\n       |\n=========\n',
        '\n  ______\n  |   \|\n  O    |\n /|\   |\n / \   |\n       |\n=========\n'
    ]
    lives = 6
    wordToFind = wTF
    underscoreArray = []
    for letter in wordToFind:
        underscoreArray.append("_")
    underscoreString = ""
    checkingString = ""
    for item in underscoreArray:
        underscoreString += str(item) + " "
        checkingString += str(item)
    underscoreString = underscoreString[:len(underscoreString)-1]
    while lives > 0:

        print(hangmanAsciiGraphics[6 - lives])
        question = "Let's guess the word: " + underscoreString + " "
        userInput = input(question)
        if userInput in wordToFind:
            for i in range(len(wordToFind)):
                if wordToFind[i] == userInput:
                    underscoreArray[i] = userInput
            underscoreString = ""
            checkingString = ""
            for item in underscoreArray:
                underscoreString += str(item) + " "
                checkingString += str(item)
            # print(checkingString)
            underscoreString = underscoreString[:len(underscoreString) - 1]
        if checkingString == wordToFind:
            print("You won!")
            break
        if userInput not in wordToFind:
            lives -= 1
    if lives == 0:
        print(hangmanAsciiGraphics[6])
        print("YOU LOSE")

words = []
src = open("hangman_words.txt","r")
for line in src.readlines():
    words.append(line.split("\n")[0])
src.close()
randomWordFromFile = words[randrange(len(words))]


hangman_without_graphics(randomWordFromFile)

