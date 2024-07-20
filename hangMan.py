import random
# import tkinter as tk
# from tkinter import messagebox

def display_hangman(attempts_left):
    """Display the hangman ASCII art based on the number of attempts left."""
    stages = [
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        =========
        """,
        # """
        #    -----
        #    |   |
        #    O   |
        #   /|\\  |
        #   /    |
        #        |
        # =========
        # """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        =========
        """,
        # """
        #    -----
        #    |   |
        #    O   |
        #   /|   |
        #        |
        #        |
        # =========
        # """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        =========
        """,
        """
           -----
           |   |
               |
               |
               |
               |
        =========
        """
    ]
    return stages[attempts_left]

def hangman():
    words = [
        ("apple", "guess the fruit which keeps doctor away?"),
        ("banana", "a long yellow fruit"),
        ("cherry", "small, round, and red fruit"),
        ("grape", "used to make wine"),
        ("orange", "a citrus fruit"),
        ("pineapple", "a tropical fruit with a spiky exterior"),
        ("strawberry", "small, red, and delicious"),
        ("mango", "sweet and tropical fruit"),
        ("blueberry", "small and blue, often used in muffins"),
        ("watermelon", "large and green with red interior")
    ]
    
    play_again = "yes"
    while play_again.lower() == "yes":
        word_to_guess, hint = random.choice(words)
        guessed_letters = set()
        attempts_left = 4

        print("Welcome to Hangman!")
        print("Try to guess the word within 5 attempts.")

        while attempts_left > 0:
            # Generate a hint
            print(hint)
            hint = ""
            for letter in word_to_guess:
                if letter in guessed_letters:
                    hint += letter + " "
                else:
                    hint += "_ "
            print("Guess the word:", hint)
            print(display_hangman(attempts_left))

            guess = input("Guess a letter or the entire word: ").lower()

            if not guess.isalpha():
                print("Invalid input. Please enter a letter or a word.")
                continue

            if len(guess) == 1:  # Guessing a letter
                if guess in guessed_letters:
                    print(f"You already guessed '{guess}'. Try again.")
                    continue

                guessed_letters.add(guess)

                if guess in word_to_guess:
                    print(f"Correct! '{guess}' is in the word.")
                else:
                    print(f"Wrong guess! '{guess}' is not in the word.")
                    attempts_left -= 1

            elif len(guess) == len(word_to_guess) and guess == word_to_guess:  # Guessing the entire word
                print(f"Congratulations! You guessed the word: {word_to_guess}")
                break

            else:
                print("Incorrect guess!")
                attempts_left -= 1

            print(f"Attempts left: {attempts_left}")

        else:
            print(display_hangman(0))
            print("You ran out of attempts! The word was:", word_to_guess)

        play_again = input("Do you want to play again? (yes/no): ")

    print("Thanks for playing!")

# Start the game
hangman()
