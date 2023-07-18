from tkinter import *
import random

BG_C = "#3b3b3b"
MAXTRIES = 5
attempt = 0

root = Tk()
root.title("Wordle")
root.resizable(False, False)
root.geometry("400x500")
root.config(bg=BG_C)

def playRW():
    for i in root.winfo_children(): i.destroy()
    def getWord(file):
        with open(file, 'r') as f: wordList = f.readlines()
        return random.choice(wordList)
    def checkAndDisplay(word, guessL, gameState):
        def wordStats(word, gus):
            feedback = ""
            for i in range(len(gus)):
                guess_char = gus[i]
                word_char = word[i]

                if guess_char == word_char:
                    feedback += 'X'  # Letter is in the correct position.
                elif guess_char in word:
                    feedback += 'O'  # Letter is in the word but not in the correct position.
                else:
                    feedback += '-'  # Letter is not in the word.
            return feedback
        def winLoss(gameState):
            for widget in root.winfo_children():
                    if isinstance(widget, Label):
                        if widget.cget('text') == "Wordle": pass
                        else: widget.destroy()

            frame = Frame(root, bg="white")
            frame.place(x=10, y=80, width=380, height=325)
            if gameState == "W":
                Label(frame, text="Your won! Congrats", font=('arial', 30)).place(x=10, y=5)
            elif gameState == "L":
                Label(frame, text="You lost :(", font=('arial', 30)).place(x=100, y=5)
            Label(frame, text=f"The word was: {word.upper()}", font=('arial', 25)).place(x=20, y=55)

            Button(frame, text="Again", font=('arial', 25), command=playRW).place(x=10, y=200, width=150, height=45)
            Button(frame, text="Main Menu", font=('arial', 20), command=mainScreen).place(x=220, y=200, width=150, height=45)

        global MAXTRIES, attempt
        sX, sY = 65, 100
        sW, sH = 50, 50

        for i, guess in enumerate(guessL):
            feedback = wordStats(word, guess)
            if feedback == "XXXXX":
                gameState = "W"
                winLoss(gameState)
            elif MAXTRIES == attempt:
                gameState = "L"
                winLoss(gameState)

            if gameState == "P":
                Label(root, text=f"{i+1}.", font=('arial', 35), fg="#ffffff", bg=BG_C).place(x=sX-50, y=sY, width=sW, height=sH)
                for j, letter in zip(feedback, guess):
                    if j == "X": Label(root, text=letter.upper(), font=('arial', 40, 'bold'), bg="#00ff00").place(x=sX+10, y=sY, width=sW, height=sH)
                    elif j == "O": Label(root, text=letter.upper(), font=('arial', 40, 'bold'), bg="#fff000").place(x=sX+10, y=sY, width=sW, height=sH)
                    else: Label(root, text=letter.upper(), font=('arial', 40, 'bold'), bg=BG_C, fg="white").place(x=sX+10, y=sY, width=sW, height=sH)
                    sX += 60
                sX = 65
                sY += 55
    def checkWord(e):
        if len(guess.get()) == 5:
            global attempt
            attempt += 1
            guessL.append(guess.get().lower())
            checkAndDisplay(word, guessL, gameState)
            guess.delete(0, END)
        else:
            print("No")

    global attempt
    attempt = 0
    guessL = []
    gameState = "P"
    word = getWord("words.txt")
    
    Label(root, text="Wordle", font=('arial', 35), bg=BG_C, fg="white").place(x=125, y=10)

    guess = Entry(root, font=('arial', 30), justify='center', bg='#525254', borderwidth=1)
    guess.place(x=15, y=435, height=50, width=370)
    guess.bind("<Return>", checkWord)
def playCW(word):
    for i in root.winfo_children(): i.destroy()

    def checkAndDisplay(word, guessL, gameState):
        def wordStats(word, gus):
            feedback = ""
            for i in range(len(gus)):
                guess_char = gus[i]
                word_char = word[i]

                if guess_char == word_char:
                    feedback += 'X'  # Letter is in the correct position.
                elif guess_char in word:
                    feedback += 'O'  # Letter is in the word but not in the correct position.
                else:
                    feedback += '-'  # Letter is not in the word.
            return feedback
        def winLoss(gameState):
            for widget in root.winfo_children():
                    if isinstance(widget, Label):
                        if widget.cget('text') == "Wordle": pass
                        else: widget.destroy()

            frame = Frame(root, bg="white")
            frame.place(x=10, y=80, width=380, height=325)
            if gameState == "W":
                Label(frame, text="Your won! Congrats", font=('arial', 30)).place(x=10, y=5)
            elif gameState == "L":
                Label(frame, text="You lost :(", font=('arial', 30)).place(x=100, y=5)
            Label(frame, text=f"The word was: {word.upper()}", font=('arial', 25)).place(x=20, y=55)

            Button(frame, text="Again", font=('arial', 25), command=playRW).place(x=10, y=200, width=150, height=45)
            Button(frame, text="Main Menu", font=('arial', 20), command=mainScreen).place(x=220, y=200, width=150, height=45)

        global MAXTRIES, attempt
        sX, sY = 65, 100
        sW, sH = 50, 50

        for i, guess in enumerate(guessL):
            feedback = wordStats(word, guess)
            if feedback == "XXXXX":
                gameState = "W"
                winLoss(gameState)
            elif MAXTRIES == attempt:
                gameState = "L"
                winLoss(gameState)

            if gameState == "P":
                Label(root, text=f"{i+1}.", font=('arial', 35), fg="#ffffff", bg=BG_C).place(x=sX-50, y=sY, width=sW, height=sH)
                for j, letter in zip(feedback, guess):
                    if j == "X": Label(root, text=letter.upper(), font=('arial', 40, 'bold'), bg="#00ff00").place(x=sX+10, y=sY, width=sW, height=sH)
                    elif j == "O": Label(root, text=letter.upper(), font=('arial', 40, 'bold'), bg="#fff000").place(x=sX+10, y=sY, width=sW, height=sH)
                    else: Label(root, text=letter.upper(), font=('arial', 40, 'bold'), bg=BG_C, fg="white").place(x=sX+10, y=sY, width=sW, height=sH)
                    sX += 60
                sX = 65
                sY += 55
    def checkWord(e):
        if len(guess.get()) == 5:
            global attempt
            attempt += 1
            guessL.append(guess.get().lower())
            checkAndDisplay(word, guessL, gameState)
            guess.delete(0, END)
        else:
            print("No")

    global attempt
    attempt = 0
    guessL = []
    gameState = "P"
    
    Label(root, text="Wordle", font=('arial', 35), bg=BG_C, fg="white").place(x=125, y=10)

    guess = Entry(root, font=('arial', 30), justify='center', bg='#525254', borderwidth=1)
    guess.place(x=15, y=435, height=50, width=370)
    guess.bind("<Return>", checkWord)

def createGame():
    for i in root.winfo_children(): i.destroy()
    def createWord():
        if len(wordE.get()) == 5:
            text = wordE.get().lower()
            shift = 5
            encrypted_text = ""
            for char in text:
                if char.isalpha():
                    if char.isupper():
                        encrypted_char = chr((ord(char) - 65 + shift) % 26 + 65)
                    else:
                        encrypted_char = chr((ord(char) - 97 + shift) % 26 + 97)
                else:
                    encrypted_char = char
                encrypted_text += encrypted_char
            outputE.delete(0, END)
            outputE.insert(0, encrypted_text)



    Label(root, text="Wordle", font=('arial', 35), bg=BG_C, fg="white").place(x=125, y=10)

    Label(root, text="Word", font=('arial', 30), bg=BG_C, fg="white").place(x=15, y=90)
    wordE = Entry(root, font=('arial', 29), justify='center')
    wordE.place(x=150, y=95, width=220, height=45)

    Button(root, text="Create", font=('arial', 30), command=createWord).place(x=10, y=150, width=380, height=50)

    Label(root, text="Output", font=('arial', 30), bg=BG_C, fg="white").place(x=15, y=215)
    outputE = Entry(root, font=('arial', 29), justify='center')
    outputE.place(x=150, y=220, width=220, height=45)


    Button(root, text="Back", font=('arial', 30), command=mainScreen).place(x=10, y=440, width=380, height=50)

def playCode():
    for i in root.winfo_children(): i.destroy()
    def play():
        if len(wordE.get()) == 5:
            text = wordE.get().lower()
            shift = -5
            encrypted_text = ""
            for char in text:
                if char.isalpha():
                    if char.isupper():
                        encrypted_char = chr((ord(char) - 65 + shift) % 26 + 65)
                    else:
                        encrypted_char = chr((ord(char) - 97 + shift) % 26 + 97)
                else:
                    encrypted_char = char
                encrypted_text += encrypted_char
            playCW(encrypted_text)


    Label(root, text="Wordle", font=('arial', 35), bg=BG_C, fg="white").place(x=125, y=10)
    
    Label(root, text="Code", font=('arial', 30), bg=BG_C, fg="white").place(x=15, y=140)
    wordE = Entry(root, font=('arial', 29), justify='center')
    wordE.place(x=150, y=145, width=220, height=45)

    Button(root, text="Play", font=('arial', 27), command=play).place(x=10, y=200, width=380, height=50)
    Button(root, text="Back", font=('arial', 30), command=mainScreen).place(x=10, y=440, width=380, height=50)

def mainScreen():
    for i in root.winfo_children(): i.destroy()
    Label(root, text="Wordle", font=('arial', 35), bg=BG_C, fg="white").place(x=125, y=10)

    Button(root, text="Play", font=("Arial", 30), command=playRW).place(x=15, y=130, width=370, height=50)
    Button(root, text="Create", font=("Arial", 25), command=createGame).place(x=15, y=245, width=370, height=50)
    Button(root, text="Play with code", font=("Arial", 25), command=playCode).place(x=15, y=310, width=370, height=50)


mainScreen()

root.mainloop()

