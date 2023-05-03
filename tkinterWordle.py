from colorama import Fore, Style
from tkinter import *
import colorama
import random

colorama.init()

root = Tk()
root.title("Wordle")
root.geometry("350x550")
root.resizable(False, False)
root.config(bg='#525254')

def display_word(guessL, ans):
    sX, sY = 60, 100
    for j, guess in enumerate(guessL):
        Label(root, text=f"{j+1}.", font=('arial', 35), fg="#ffffff", bg='#525254').place(x=sX-50, y=sY)
        cl, cp = check_correct_position(ans, guess)
        for i, letter in enumerate(guess):
            if letter in cl:
                if i in cp:
                    Label(root, text=f"{letter}", font=('arial', 35), fg="#00ff00", bg='#525254').place(x=sX+10, y=sY)
                else:
                    Label(root, text=letter, font=('arial', 35), fg="#fff000", bg='#525254').place(x=sX+10, y=sY)
            else:
                Label(root, text=letter, font=('arial', 35), fg="#ffffff", bg='#525254').place(x=sX+10, y=sY)
            sX += 50
        sX = 60
        sY += 50

def check_correct_position(ans, guess):
    cl = []
    cp = []
    for i, letter in enumerate(guess):
        if letter == ans[i]:
            cl.append(letter)
            cp.append(i)
        elif letter in ans:
            cl.append(letter)
    return cl, cp

MAXTRIES = 2
attempt = 0
score = 0

def game():
    for widget in root.winfo_children(): widget.destroy()
    global MAXTRIES, attempt
    
    MAXTRIES, attempt = 5, 0
    words, guessL = [], []
    
    with open("words.txt", 'r') as f:
        for line in f: words.append(line.strip('\n').upper())
        
    word = random.choice(words)

    #print(word)
    def checkGuess(event):
        global MAXTRIES, attempt, score
        if len(guess.get()) == 5:
            guessL.append(guess.get().upper())
            if guess.get().upper() == word:
                guess.destroy()
                score += 1
                root.title(f"Wordle | Score: {score}")
                Label(root, text="You Won", font=('arial', 30), fg='#ffffff', bg='#525254').place(x=10, y=500)
                Button(root, text="Again?", font=('arial', 25), command=game).place(x=200, y=500, height=45, width=145)
            elif attempt >= MAXTRIES:
                guess.destroy()
                Label(root, text="You Lost", font=('arial', 30), fg='#ffffff', bg='#525254').place(x=10, y=500)
                Label(root, text=f"Word: {word}", font=('arial', 30), fg='#ffffff', bg='#525254').place(x=35, y=430)
                Button(root, text="Again?", font=('arial', 25), command=game).place(x=200, y=500, height=45, width=145)
            display_word(guessL, word)
            guess.delete(0, END)
            attempt += 1

    Label(root, text="Wordle", font=('arial', 30), fg='#ffffff', bg='#525254').place(x=110, y=10)
    guess = Entry(root, font=('arial', 25), justify='center')
    guess.place(x=75, y=500, height=40, width=200)
    guess.bind("<Return>", checkGuess)

game()

root.mainloop()
