import tkinter as tk
from tkinter import messagebox
import random

class HangmanGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Hangman Game")
        
        self.word = self.choose_word()
        self.guessed_letters = []
        self.attempts = 6
        
        self.word_label = tk.Label(master, text=self.display_word(), font=("Helvetica", 24))
        self.word_label.pack(pady=20)
        
        self.input_label = tk.Label(master, text="Enter a letter:", font=("Helvetica", 14))
        self.input_label.pack()
        
        self.input_entry = tk.Entry(master, width=10, font=("Helvetica", 14))
        self.input_entry.pack(pady=10)
        
        self.guess_button = tk.Button(master, text="Guess", command=self.guess_letter)
        self.guess_button.pack()
        
    def choose_word(self):
        words = ['python', 'hangman', 'programming', 'computer', 'science', 'algorithm', 'software', 'development']
        return random.choice(words)
    
    def display_word(self):
        display = ''
        for letter in self.word:
            if letter in self.guessed_letters:
                display += letter + ' '
            else:
                display += '_ '
        return display
    
    def guess_letter(self):
        guess = self.input_entry.get().lower()
        self.input_entry.delete(0, tk.END)
        
        if len(guess) != 1 or not guess.isalpha():
            messagebox.showerror("Error", "Please enter a single letter.")
            return
        
        if guess in self.guessed_letters:
            messagebox.showinfo("Info", "You've already guessed that letter.")
            return
        
        self.guessed_letters.append(guess)
        
        if guess not in self.word:
            self.attempts -= 1
            messagebox.showinfo("Incorrect", f"'{guess}' is not in the word. You have {self.attempts} attempts left.")
        else:
            messagebox.showinfo("Correct", f"'{guess}' is in the word.")
        
        self.update_display()
        
        if all(letter in self.guessed_letters for letter in self.word):
            messagebox.showinfo("Congratulations", f"Congratulations! You've guessed the word: {self.word}")
            self.master.destroy()
        elif self.attempts == 0:
            messagebox.showinfo("Game Over", f"Sorry, you ran out of attempts. The word was: {self.word}")
            self.master.destroy()
    
    def update_display(self):
        self.word_label.config(text=self.display_word())

def main():
    root = tk.Tk()
    app = HangmanGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
