import random
import tkinter as tk
from tkinter import messagebox

def check_guess():
    global attempts
    try:
        guess = int(guess_entry.get())
        if guess < secret_number:
            result_label.config(text="Too low! Try guessing higher.", fg="orange")
        elif guess > secret_number:
            result_label.config(text="Too high! Try guessing lower.", fg="orange")
        else:
            messagebox.showinfo("Congratulations!", f"You've guessed the number ({secret_number}) in {attempts + 1} attempts!")
            root.destroy()
            return
        attempts += 1
        attempts_left = max_attempts - attempts
        attempts_label.config(text=f"Attempts left: {attempts_left}",fg="red",bg="skyblue")
        if attempts_left == 0:
            messagebox.showinfo("Game Over", f"Sorry, you've run out of attempts. The number was {secret_number}.")
            root.destroy()
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.",fg="blue")
    finally:
        guess_entry.delete(0, tk.END)

def close_game():
    messagebox.showinfo("Game Over", f"The number was {secret_number}.")
    root.destroy()

def number_guessing_game():
    global secret_number, attempts, max_attempts, guess_entry, result_label, attempts_label, root

    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 5

    root = tk.Tk()
    root.title("Number Guessing Game")
    root.configure(bg="skyblue")

    header_label = tk.Label(root, text="Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.",fg="green",bg="skyblue")
    header_label.pack()

    guess_entry = tk.Entry(root)
    guess_entry.pack()

    submit_button = tk.Button(root, text="Submit Guess",fg="blue",bg="yellow", command=check_guess)
    submit_button.pack()

    result_label = tk.Label(root, text="",bg="skyblue")
    result_label.pack()

    attempts_left = max_attempts - attempts
    attempts_label = tk.Label(root, text=f"Attempts left: {attempts_left}",fg="red",bg="skyblue")
    attempts_label.pack()

    close_button = tk.Button(root, text="Close Game",fg="blue",bg="yellow", command=close_game)
    close_button.pack()

    root.mainloop()

number_guessing_game()
