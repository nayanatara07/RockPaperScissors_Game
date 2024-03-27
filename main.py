import random
import tkinter as tk
from tkinter import messagebox

options = ("Rock", "Paper", "Scissors")

def play_game():
    player = input_entry.get().capitalize()
    computer = random.choice(options)

    result = f"Player: {player}\nComputer: {computer}\n"

    if player == computer:
        result += "It's a tie!"
    elif (player == "Rock" and computer == "Scissors") or (player == "Paper" and computer == "Rock") or (player == "Scissors" and computer == "Paper"):
        result += "You win :)"
    else:
        result += "You lost :("

    messagebox.showinfo("Result", result)

root = tk.Tk()
root.title("Rock Paper Scissors Game")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

label = tk.Label(frame, text="Enter a choice (Rock, Paper, Scissors):")
label.pack()

input_entry = tk.Entry(frame)
input_entry.pack()

start_button = tk.Button(frame, text="Start", command=play_game)
start_button.pack()

root.mainloop()

