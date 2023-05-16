import random

print("hangman take a guess")
print("_____________________")

wordbank = ["basketball","socker","sunflower","river","frogs","zebra"]


randomWord = random.choice(wordbank)

for x in randomWord:
    print("_", end= " ")

def print_hangman(wrong):
    if(wrong == 0):
        print("\n+---+")
        print("   |")
        print("   |")
        print("   |")
        print("  ===")
    elif(wrong == 1):
        print("\n+---+")
        print(" 0 |")
        print("   |")
        print("   |")
        print("  ===")
    elif(wrong == 2):
        print("\n+---+")
        print(" O |")
        print(" | |")
        print("   |")
        print("  ===")
    elif(wrong == 3):
        print("\n+---+")
        print(" 0 |")
        print(" | |")
        print(" ^ |")
        print("  ===")

def printWord(guessedLetters):
    counter=0
    rightletter=0
    for char in randomWord:
        if(char in guessedLetters):
            print(randomWord[counter], end=" ")
        else:
            print(" ", end=" ")
        counter+=1
    return rightletter

def printLines():
    print("\r")
    for char in randomWord:
        print("\u203E", end=" ")

length_of_word_to_guess = len(randomWord)
amount_times_wrong = 0
current_guess_index = 0
current_letters_guessed = []
current_letters_right = 0

while(amount_times_wrong !=4 and current_letters_right != length_of_word_to_guess):
    print("\n Letters guessed so far: ")
    for letter in current_letters_guessed:
        print(letter, end=" ")
    ### prompt user for input
    letterGuessed = input(" \n Guess a letter")
    ###
    if(randomWord[current_guess_index] == letterGuessed):
        print_hangman(amount_times_wrong)
    ###
        current_guess_index+=1
        current_letters_guessed.append(letterGuessed)
        current_letters_right = printWord(current_letters_guessed)
        printLines()
    ### wrong
    else:
        amount_times_wrong+=1
        current_letters_guessed.append(letterGuessed)
        ### up date
        print_hangman(amount_times_wrong)
        ### print word
        current_letters_right = printWord(current_letters_guessed)
        printLines()

print("GAME is over ")