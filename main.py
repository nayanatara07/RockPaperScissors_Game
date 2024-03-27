import random
import tkinter as tk
from tkinter import messagebox

# Define the options globally
options = ("Rock", "Paper", "Scissors")

# Function to play the game
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

# Creating the main window
root = tk.Tk()
root.title("Rock Paper Scissors Game")

# Adding a colorful background
root.configure(bg="lightblue")

# Creating a frame to hold the input elements
frame = tk.Frame(root, padx=20, pady=20, bg="#76c893")
frame.pack()

# Adding a label for instructions
label = tk.Label(frame, text="Enter your choice (Rock, Paper, Scissors):", bg="#76c893")
label.pack()

# Adding an entry field for user input
input_entry = tk.Entry(frame, width=30)
input_entry.pack()

# Adding a button to start the game
start_button = tk.Button(frame, text="Start", command=play_game, width=15, bg="lightgreen")
start_button.pack()

# Running the main event loop
root.mainloop()




