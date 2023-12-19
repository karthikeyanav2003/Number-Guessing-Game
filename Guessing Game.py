import tkinter as tk
from tkinter import ttk
from functools import partial
from tkinter import messagebox
import random

def initialize_game():
    global secret_number, attempts, last_guess
    secret_number = random.randint(1, 100)
    attempts = 0
    last_guess = None
    result_label1.config(text="Guess the number between 1 and 100")
    input_entry.delete(0, tk.END)
    update_attempts_label()

def guess_number(inputn):
    global attempts, last_guess
    guess = inputn.get()

    try:
        guess = int(guess)
    except ValueError:
        result_label1.config(text="Invalid input. Please enter a valid number.")
        return

    if last_guess is not None and guess == last_guess:
        result = messagebox.askquestion("Same Guess", "You entered the same number again. Is it intentional?", icon='warning')
        if result == 'no':
            result_label1.config(text="Please make a different guess.")
            return

    attempts += 1
    last_guess = guess

    if guess == secret_number:
        result_label1.config(text="Congratulations! You guessed it right.\nNumber of attempts: {}. The correct number was {}.".format(attempts, secret_number))
        show_result_message()
    elif guess < secret_number - 10:
        result_label1.config(text="Low! (Way too Low)")
    elif guess < secret_number - 5:
        result_label1.config(text="Low! (Avg Low)")
    elif guess < secret_number:
        result_label1.config(text="Low! (Near Low)")
    elif guess > secret_number + 10:
        result_label1.config(text="High! (Way too High)")
    elif guess > secret_number + 5:
        result_label1.config(text="High! (Avg High)")
    elif guess > secret_number:
        result_label1.config(text="High!  (Near High)")
    else:
        result_label1.config(text="Near the correct number. Try again.")

    update_attempts_label()

def update_attempts_label():
    attempts_label.config(text="Attempts: {}".format(attempts))

def show_result_message():
    message = "Congratulations! You guessed the correct number.\nNumber of attempts: {}\nThe correct number was {}.".format(attempts, secret_number)
    result = messagebox.askquestion("Game Over", message, icon='info')

    if result == 'yes':
        initialize_game()
    else:
        root.destroy()

root = tk.Tk()
root.geometry('500x250+700+300')
root.title('Guess the Number Game')
style = ttk.Style()
root.configure(background='#000000')
root.resizable(width=False, height=False)

style.configure('TNotebook', titlebackground='#09A3BA')

for i in range(7):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

numberInput = tk.StringVar()

input_label = tk.Label(root, text="ENTER YOUR GUESS", background='#09A3BA', foreground="#000000")
input_label.grid(row=2, column=1, sticky='e', padx=5, pady=5)
input_entry = tk.Entry(root, textvariable=numberInput, bd=2, relief="solid")
input_entry.grid(row=2, column=2, padx=5, pady=5)

attempts_label = tk.Label(root, text="Attempts: 0", background='#09A3BA', foreground="#000000")
attempts_label.grid(row=3, column=1, columnspan=5, sticky='nsew', padx=5, pady=5)

result_label1 = tk.Label(root, background='#09A3BA', foreground="#000000")
result_label1.grid(row=5, column=1, columnspan=5, sticky='nsew', padx=5, pady=5)

initialize_button = tk.Button(root, text="Initialize Game", command=initialize_game, background='#09A3BA', foreground="#000000", bd=2, relief="solid")
initialize_button.grid(row=1, column=0, columnspan=7, padx=5, pady=5)

guess_button = tk.Button(root, text="Make Guess", command=partial(guess_number, numberInput), background='#09A3BA', foreground="#000000", bd=2, relief="solid")
guess_button.grid(row=4, column=0, columnspan=7, padx=5, pady=5)

initialize_game()

root.mainloop()
