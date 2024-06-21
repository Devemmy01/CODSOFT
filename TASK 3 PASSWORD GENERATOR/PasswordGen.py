import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length, difficulty):
    if difficulty == "Easy":
        characters = string.ascii_letters + string.digits
    elif difficulty == "Medium":
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generatePassword_btn_click():
    length = int(lengthEntry.get())
    difficultyL = difficulty.get()
    password = generate_password(length, difficulty)
    messagebox.showinfo("Generated Password", password)

window = tk.Tk()
window.title("Password Generator")

window.geometry("500x300")  # to increase the width and height of the popup window
window.resizable(False, False)  # to prevent the window from being resized

lengthLabel = tk.Label(window, text="Password Length:")
lengthLabel.pack()
lengthEntry = tk.Entry(window)
lengthEntry.pack()

difficultyLabel = tk.Label(window, text="Password Difficulty:")
difficultyLabel.pack()

difficulty = tk.StringVar()
difficulty.set("Easy")

easy = tk.Radiobutton(window, text="Easy", variable=difficulty, value="Easy")
easy.pack()

medium = tk.Radiobutton(window, text="Medium", variable=difficulty, value="Medium")
medium.pack()

hard = tk.Radiobutton(window, text="Hard", variable=difficulty, value="Hard")
hard.pack()

genBtn = tk.Button(window, text="Generate Password", command=generatePassword_btn_click)
genBtn.pack()

window.mainloop()
