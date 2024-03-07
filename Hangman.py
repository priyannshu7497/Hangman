import random

def choose_word():
    words = ['python', 'hangman', 'programming', 'computer', 'science', 'algorithm', 'software', 'development']
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
    return display

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print("Try to guess the word. You have 6 attempts.")

    while attempts > 0:
        print("\nWord:", display_word(word, guessed_letters))
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempts -= 1
            print(f"Sorry, '{guess}' is not in the word. You have {attempts} attempts left.")
        else:
            print(f"Good guess! '{guess}' is in the word.")

        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You've guessed the word:", word)
            break

    if attempts == 0:
        print("\nSorry, you ran out of attempts. The word was:", word)

if __name__ == "__main__":
    hangman()
