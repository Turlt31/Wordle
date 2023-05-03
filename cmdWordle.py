from colorama import Fore, Style
import colorama
import random
import os

colorama.init(autoreset=True)
os.system('cls')

MAXTRIES = 6
attempt = 0
words = []
with open("words.txt", 'r') as f:
    for line in f:
        words.append(line.strip('\n').upper())
word = random.choice(words)
guessList = []

def print_word(wordL, ans):
    for j, word in enumerate(wordL):
        print("   -----------")
        print(f"{j+1}. ", end="")
        print("|", end="")
        cl, cp = check_correct_position(ans, word)
        for i, letter in enumerate(word):
            if letter in cl:
                if i in cp:
                    print(Fore.GREEN + letter + Style.RESET_ALL, end="|")
                else:
                    print(Fore.YELLOW + letter + Style.RESET_ALL, end="|")
            else:
                print(Style.RESET_ALL + letter + Style.RESET_ALL, end="|")
        print(Style.RESET_ALL)

def check_correct_position(word, guess):
    correct_letters = []
    correct_positions = []
    for i, letter in enumerate(guess):
        if letter == word[i]:
            correct_letters.append(letter)
            correct_positions.append(i)
        elif letter in word:
            correct_letters.append(letter)
    return correct_letters, correct_positions

    
def get_guess():
    guess = input("\nGuess: ").upper()
    if len(guess) > 5 or len(guess) < 5:
        print("Your guess must be 5 letters")
        input("Press ENTER to try again")
        os.system('cls')
        get_guess()
    else:
        return guess

while attempt != MAXTRIES:
    guess = get_guess()
    
    guessList.append(guess)
    os.system('cls')
    print_word(guessList, word)

    if guess == word:
        print("You got it!")
        break

    attempt += 1

print(f"\nThe word was: {word}")
