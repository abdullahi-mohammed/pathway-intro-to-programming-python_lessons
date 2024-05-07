# Author: Abdullahi Mohammed
# Date:   3rd, feb. 2024.
# Purpose: Word Puzzle Game
# Stretch Challenge: I implemented a check to verify if the guessed word contains only alphabet. And if not, an error is displayed to the Player.


# Hint Word - FAMILY
# Welcome to the word guessing game!

# Your hint is: _ _ _ _ _ _ 
# What is your guess? temple
# Your hint is: _ _ m _ _ _ 
# What is your guess? moroni
# Your hint is: M O _ o _ i 
# What is your guess? hhhhhh
# Your hint is: h h h h h H 
# What is your guess? mosiah  
# Congratulations! You guessed it!
# It took you 4 guesses.

secret_word = "FAMILY"
secret_word_length = len(secret_word)
guessed_word = []
print("Welcome to the word guessing game!\n")
print("Your hint is: ", end=" ")
for letter in secret_word:
    print("_ ", end=" ")
print("")

for word in range(secret_word_length):
    guess = input("What is your guess? ")

    # check if guessed word contains only alphabet
    if not guess.isalpha():
        print("Please enter only letters.")
        continue

    if len(guess) != secret_word_length:
        print("Sorry, the guess must have the same number of letters as the secret word.")
        if word + 1 == secret_word_length:
            print(f"It took you {word + 1} guesses.")
    else:
        for i, letter in enumerate(guess):
            # showing Letters that are present in the secret word at that exact spot spot (uppercase).
            if letter.upper() == secret_word[i].upper():
                correct_letter = secret_word[i].upper()
                guessed_word.append(correct_letter)

            # Showing Letters that are present in the secret word, but in a different spot (lowercase).
            elif letter.upper() in secret_word.upper():
                correct_letter = secret_word[secret_word.lower().find(letter.lower())].lower()
                guessed_word.append(correct_letter)

            # Showing _ for letters that are not present in the secret word
            else:
                guessed_word.append("_")

    if guess.upper() == secret_word:
        print("Congratulations! You guessed it!")
        # guess count
        print(f"It took you {word + 1} guesses.")
        break
    else:
        print("Your hint is: ", " ".join(guessed_word))
    guessed_word = []