import random
import tkinter as tk
from tkinter import messagebox

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    result_text.set(f"You chose {user_choice.capitalize()}.\nComputer chose {computer_choice.capitalize()}.")

    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
            (user_choice == 'rock' and computer_choice == 'scissors') or
            (user_choice == 'paper' and computer_choice == 'rock') or
            (user_choice == 'scissors' and computer_choice == 'paper')
    ):
        user_score_var.set(user_score_var.get() + 1)
        return "You win!"
    else:
        computer_score_var.set(computer_score_var.get() + 1)
        return "Computer wins!"

def play_game(user_choice):
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    result_text.set(result)

    user_label_var.set(f"Your Choice: {user_choice.capitalize()}")
    
    score_text.set(f"Score: You {user_score_var.get()} - {computer_score_var.get()} Computer")
    
    play_again_button.pack(side="left", padx=10)
    
    root.update_idletasks()
    root.update()

def reset_scores():
    user_score_var.set(0)
    computer_score_var.set(0)
    score_text.set("Score: You 0 - 0 Computer")
    result_text.set("")
    user_label_var.set("Your Choice: ")
    play_again_button.pack_forget()

def play_again():
    user_label_var.set("Your Choice: ")
    result_text.set("")
    play_again_button.pack_forget()

# Tkinter GUI
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("400x300")
root.resizable(False, False)
root.configure(bg="#f0f0f0")

# Variables
user_choice_var = tk.StringVar()
user_score_var = tk.IntVar()
computer_score_var = tk.IntVar()
user_label_var = tk.StringVar()

# Create and pack GUI elements
user_label = tk.Label(root, textvariable=user_label_var, bg="#f0f0f0", font=("Arial", 12))
user_label.pack(pady=5)

rock_button = tk.Button(root, text="Rock", command=lambda: play_game("rock"), bg="#b3e0ff", font=("Arial", 10))
rock_button.pack(side="left", padx=10)
paper_button = tk.Button(root, text="Paper", command=lambda: play_game("paper"), bg="#ffb3b3", font=("Arial", 10))
paper_button.pack(side="left", padx=10)
scissors_button = tk.Button(root, text="Scissors", command=lambda: play_game("scissors"), bg="#b3ffb3", font=("Arial", 10))
scissors_button.pack(side="left", padx=10)

result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, bg="#f0f0f0", font=("Arial", 12, "italic"))
result_label.pack(pady=5)

score_text = tk.StringVar()
score_label = tk.Label(root, textvariable=score_text, bg="#f0f0f0", font=("Arial", 12, "bold"))
score_label.pack()

reset_scores_button = tk.Button(root, text="Reset Scores", command=reset_scores, bg="#ff6666")
reset_scores_button.pack(side="left", padx=10)

play_again_button = tk.Button(root, text="Play Again", command=play_again, bg="#ccffcc")
play_again_button.pack_forget()

user_score_var.set(0)
computer_score_var.set(0)
score_text.set("Score: You 0 - 0 Computer")
user_label_var.set("Your Choice: ")

# Run the GUI
root.mainloop()
