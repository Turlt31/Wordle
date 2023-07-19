from tkinter import *
import random
import re

BG_C = "#3b3b3b"
MAXTRIES = 5

attempt = 0
keyboard = True
greenL = []
yellowL = []
greyL = []


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
            frame.place(x=10, y=70, width=380, height=355)
            if gameState == "W":
                Label(frame, text="You won! Congrats", font=('arial', 30), bg="white").place(x=10, y=5)
            elif gameState == "L":
                Label(frame, text="You lost :(", font=('arial', 30), bg="white").place(x=100, y=5)
            Label(frame, text=f"The word was: {word.upper()}", font=('arial', 25), bg="white").place(x=20, y=55)

            Button(frame, text="Again", font=('arial', 25), command=playRW).place(x=10, y=100, width=150, height=45)
            Button(frame, text="Main Menu", font=('arial', 20), command=mainScreen).place(x=220, y=100, width=150, height=45)

            sX, sY = 90, 155
            sW, sH = 35, 35
            for i in feedbackL:
                for j in i:
                    if j == "X": Label(frame, text=" ", font=('arial', 40, 'bold'), bg="#00ff00").place(x=sX+10, y=sY, width=sW, height=sH)
                    elif j == "O": Label(frame, text=" ", font=('arial', 40, 'bold'), bg="#fff000").place(x=sX+10, y=sY, width=sW, height=sH)
                    else: Label(frame, text=" ", font=('arial', 40, 'bold'), bg=BG_C, fg="white").place(x=sX+10, y=sY, width=sW, height=sH)
                    sX += 40
                sX = 90
                sY += 40

        global MAXTRIES, attempt
        global greenL, yellowL, greyL
        feedbackL = []
        sX, sY = 65, 100
        sW, sH = 50, 50

        for i, guess in enumerate(guessL):
            feedback = wordStats(word, guess)
            feedbackL.append(feedback)
            if feedback == "XXXXX":
                gameState = "W"
                winLoss(gameState)
            elif MAXTRIES == attempt:
                gameState = "L"
                winLoss(gameState)

            if gameState == "P":
                Label(root, text=f"{i+1}.", font=('arial', 35), fg="#ffffff", bg=BG_C).place(x=sX-50, y=sY, width=sW, height=sH)
                for j, letter in zip(feedback, guess):
                    if j == "X": Label(root, text=letter.upper(), font=('arial', 40, 'bold'), bg="#00ff00").place(x=sX+10, y=sY, width=sW, height=sH); greenL.append(letter.upper())
                    elif j == "O": Label(root, text=letter.upper(), font=('arial', 40, 'bold'), bg="#fff000").place(x=sX+10, y=sY, width=sW, height=sH); yellowL.append(letter.upper())
                    else: Label(root, text=letter.upper(), font=('arial', 40, 'bold'), bg=BG_C, fg="white").place(x=sX+10, y=sY, width=sW, height=sH); greyL.append(letter.upper())
                    sX += 60
                sX = 65
                sY += 55

        if keyboard:
            displayKeyboard(keyS)
    def checkWord(e):
        if len(guess.get()) == 5 and not re.search(r'[0-9\W]', guess.get()):
            global attempt
            attempt += 1
            guessL.append(guess.get().lower())
            checkAndDisplay(word, guessL, gameState)
            guess.delete(0, END)
        else:
            print("No")
    def displayKeyboard(keyS):
        global greenL, yellowL, greyL
        qwerty_layout = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]

        max_row_length = max(len(row) for row in qwerty_layout)
        window_width = max_row_length * 50

        for row, row_keys in enumerate(qwerty_layout):
            row_width = len(row_keys) * 50
            x_offset = (window_width - row_width) // 2
            for col, key in enumerate(row_keys):
                x_pos = (x_offset + col * 50) + 25
                y_pos = (row * 50) + 25
                if key in greenL:
                    Label(keyS, text=key, font=("Helvetica", 30, 'bold'), bg="#00ff00", fg="black").place(x=x_pos, y=y_pos, width=50, height=50)
                elif key in yellowL:
                    Label(keyS, text=key, font=("Helvetica", 30, 'bold'), bg="#fff000", fg="black").place(x=x_pos, y=y_pos, width=50, height=50)
                elif key in greyL:
                    Label(keyS, text=key, font=("Helvetica", 30, 'bold'), bg="grey", fg="black").place(x=x_pos, y=y_pos, width=50, height=50)
                else:
                    Label(keyS, text=key, font=("Helvetica", 30, 'bold'), bg="#3b3b3b", fg="white").place(x=x_pos, y=y_pos, width=50, height=50)
    def exit(e): mainScreen()

    global attempt, keyboard, greenL, yellowL, greyL
    greenL, yellowL, greyL = [], [], []
    attempt = 0
    guessL = []
    gameState = "P"
    word = getWord("words.txt")
    
    if keyboard:
        keyS = Toplevel(root)
        keyS.title("Keyboard")
        keyS.geometry("550x200")
        keyS.config(bg="#3b3b3b")
        keyS.resizable(False, False)

        displayKeyboard(keyS)
    else:
        print("Keyboard will not be displayed")

    Label(root, text="Wordle", font=('arial', 35), bg=BG_C, fg="white").place(x=125, y=10)
    a = Label(root, text="Exit", font=('arial', 15), bg=BG_C, fg="grey")
    a.place(x=360, y=0)
    a.bind('<Button-1>', exit)

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
            frame.place(x=10, y=70, width=380, height=355)
            if gameState == "W":
                Label(frame, text="You won! Congrats", font=('arial', 30), bg="white").place(x=10, y=5)
            elif gameState == "L":
                Label(frame, text="You lost :(", font=('arial', 30), bg="white").place(x=100, y=5)
            Label(frame, text=f"The word was: {word.upper()}", font=('arial', 25), bg="white").place(x=20, y=55)

            Button(frame, text="Again", font=('arial', 25), command=playCode).place(x=10, y=100, width=150, height=45)
            Button(frame, text="Main Menu", font=('arial', 20), command=mainScreen).place(x=220, y=100, width=150, height=45)

            sX, sY = 90, 155
            sW, sH = 35, 35
            for i in feedbackL:
                for j in i:
                    if j == "X": Label(root, text=letter.upper(), font=('arial', 40, 'bold'), bg="#00ff00").place(x=sX+10, y=sY, width=sW, height=sH); greenL.append(letter.upper())
                    elif j == "O": Label(root, text=letter.upper(), font=('arial', 40, 'bold'), bg="#fff000").place(x=sX+10, y=sY, width=sW, height=sH); yellowL.append(letter.upper())
                    else: Label(root, text=letter.upper(), font=('arial', 40, 'bold'), bg=BG_C, fg="white").place(x=sX+10, y=sY, width=sW, height=sH); greyL.append(letter.upper())
                    sX += 40
                sX = 90
                sY += 40
            if keyboard:
                displayKeyboard(keyS)

        global MAXTRIES, attempt, keyboard
        global greenL, yellowL, greyL
        feedbackL = []
        sX, sY = 65, 100
        sW, sH = 50, 50

        for i, guess in enumerate(guessL):
            feedback = wordStats(word, guess)
            feedbackL.append(feedback)
            if feedback == "XXXXX":
                gameState = "W"
                winLoss(gameState)
            elif MAXTRIES == attempt:
                gameState = "L"
                winLoss(gameState)

            if gameState == "P":
                Label(root, text=f"{i+1}.", font=('arial', 35), fg="#ffffff", bg=BG_C).place(x=sX-50, y=sY, width=sW, height=sH)
                for j, letter in zip(feedback, guess):
                    if j == "X": Label(root, text=letter.upper(), font=('arial', 40, 'bold'), bg="#00ff00").place(x=sX+10, y=sY, width=sW, height=sH); greenL.append(letter.upper())
                    elif j == "O": Label(root, text=letter.upper(), font=('arial', 40, 'bold'), bg="#fff000").place(x=sX+10, y=sY, width=sW, height=sH); yellowL.append(letter.upper())
                    else: Label(root, text=letter.upper(), font=('arial', 40, 'bold'), bg=BG_C, fg="white").place(x=sX+10, y=sY, width=sW, height=sH); greyL.append(letter.upper())
                    sX += 60
                sX = 65
                sY += 55

        if keyboard:
            displayKeyboard(keyS)

    def checkWord(e):
        if len(guess.get()) == 5 and not re.search(r'[0-9\W]', guess.get()):
            global attempt
            attempt += 1
            guessL.append(guess.get().lower())
            checkAndDisplay(word, guessL, gameState)
            guess.delete(0, END)
        else:
            print("No")
    
    def displayKeyboard(keyS):
        global greenL, yellowL, greyL
        qwerty_layout = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]

        max_row_length = max(len(row) for row in qwerty_layout)
        window_width = max_row_length * 50

        for row, row_keys in enumerate(qwerty_layout):
            row_width = len(row_keys) * 50
            x_offset = (window_width - row_width) // 2
            for col, key in enumerate(row_keys):
                x_pos = (x_offset + col * 50) + 25
                y_pos = (row * 50) + 25
                if key in greenL:
                    Label(keyS, text=key, font=("Helvetica", 30, 'bold'), bg="#00ff00", fg="black").place(x=x_pos, y=y_pos, width=50, height=50)
                elif key in yellowL:
                    Label(keyS, text=key, font=("Helvetica", 30, 'bold'), bg="#fff000", fg="black").place(x=x_pos, y=y_pos, width=50, height=50)
                elif key in greyL:
                    Label(keyS, text=key, font=("Helvetica", 30, 'bold'), bg="grey", fg="black").place(x=x_pos, y=y_pos, width=50, height=50)
                else:
                    Label(keyS, text=key, font=("Helvetica", 30, 'bold'), bg="#3b3b3b", fg="white").place(x=x_pos, y=y_pos, width=50, height=50)
    
    def exit(e): mainScreen()

    global attempt, keyboard, greenL, yellowL, greyL
    greenL, yellowL, greyL = [], [], []
    attempt = 0
    guessL = []
    gameState = "P"
    
    if keyboard:
        keyS = Toplevel(root)
        keyS.title("Keyboard")
        keyS.geometry("550x200")
        keyS.config(bg="#3b3b3b")
        keyS.resizable(False, False)

        displayKeyboard(keyS)
    else:
        print("Keyboard will not be displayed")

    Label(root, text="Wordle", font=('arial', 35), bg=BG_C, fg="white").place(x=125, y=10)
    a = Label(root, text="Exit", font=('arial', 15), bg=BG_C, fg="grey")
    a.place(x=360, y=0)
    a.bind('<Button-1>', exit)

    guess = Entry(root, font=('arial', 30), justify='center', bg='#525254', borderwidth=1)
    guess.place(x=15, y=435, height=50, width=370)
    guess.bind("<Return>", checkWord)

def createGame():
    for i in root.winfo_children(): i.destroy()
    def createWord():
        if len(wordE.get()) == 5 and not re.search(r'[0-9\W]', wordE.get()):
            text = wordE.get().lower()
            text = text[:5].ljust(5)
            rotation_key = 3
            encrypted_chars = [chr(((ord(char) - 32 + rotation_key + i) % 95) + 32) for i, char in enumerate(text)]
            encrypted_string = ''.join(encrypted_chars)

            root.clipboard_clear()
            root.clipboard_append(encrypted_string)

            outputE.delete(0, END)
            outputE.insert(0, encrypted_string)
    
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
        if len(wordE.get()) == 5 and not re.search(r'[0-9]', wordE.get()):
            text = wordE.get().lower()
            text = text[:5].ljust(5)
            rotation_key = 3
            decrypted_chars = [ chr(((ord(char) - 32 - rotation_key - i) % 95) + 32) for i, char in enumerate(text) ]
            decrypted_string = ''.join(decrypted_chars)
            playCW(decrypted_string)


    Label(root, text="Wordle", font=('arial', 35), bg=BG_C, fg="white").place(x=125, y=10)
    
    Label(root, text="Code", font=('arial', 30), bg=BG_C, fg="white").place(x=15, y=140)
    wordE = Entry(root, font=('arial', 29), justify='center')
    wordE.place(x=150, y=145, width=220, height=45)

    Button(root, text="Play", font=('arial', 27), command=play).place(x=10, y=200, width=380, height=50)
    Button(root, text="Back", font=('arial', 30), command=mainScreen).place(x=10, y=440, width=380, height=50)

def mainScreen():
    for i in root.winfo_children(): i.destroy()
    def keyboardOnOff():
        global keyboard
        keyboard = not keyboard
        a.config(text="On" if keyboard else "Off")


    Label(root, text="Wordle", font=('arial', 35), bg=BG_C, fg="white").place(x=125, y=10)

    Button(root, text="Play", font=("Arial", 30), command=playRW).place(x=15, y=130, width=370, height=50)
    Button(root, text="Create", font=("Arial", 25), command=createGame).place(x=15, y=245, width=370, height=50)
    Button(root, text="Play with code", font=("Arial", 25), command=playCode).place(x=15, y=310, width=370, height=50)

    Label(root, text="Keyboard", font=("arial", 30), bg=BG_C, fg="white").place(x=15, y=435)
    a = Button(root, font=('arial', 30), command=keyboardOnOff)
    a.place(x=250, y=440, height=45, width=100)

    if keyboard: a.config(text="On")
    else: a.config(text="Off")


mainScreen()

root.mainloop()