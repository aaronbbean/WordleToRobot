"""This came makes wordle and moves a car based on the results"""


from tkinter import *
from tkinter import messagebox
root = Tk()
word = "makes"
guesscount = 0
WHITE = "#ffffff"
GREEN = "#007d21"
YELLOW ="#e2e600"
BLACK = "#000000"

root.config(bg=BLACK)
wordInput = Entry(root)
wordInput.grid(row=999, column=0, padx=10, pady=10,columnspan=3)

def getGuess():
    global word
    guess = wordInput.get()

    global guesscount 
    guesscount += 1
    if guesscount <= 5:
            
        if len(guess) == 5:
            if guess == word:
            
                messagebox.showinfo("thats it","you win!!!!!!")
            else:
                for i, letter in enumerate(guess):
                    label = Label(root, text=letter.upper())
                    label.grid(row=guesscount,column=i,padx=10,pady=10)
                    if letter in word:
                    
                        if letter == word[i]:
                            label.config(bg=GREEN,fg=BLACK)
                        else:
                            label.config(bg=YELLOW,fg=BLACK)
                    else:
                        label.config(bg=BLACK,fg=WHITE)
        else:
            messagebox.showerror("error","hey stupid it has to be 5 letters")
    else:
        messagebox.showinfo("OH NO!!", f"You lose! the word was {word}")
    

wordGuessButton = Button(root, text="Guess",command=getGuess)
wordGuessButton.grid(row=999, column=4, columnspan=2)

root.mainloop()
