import random

words = ["apple", "tiger", "house", "water", "chair"]

word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

print("Welcome to Hangman!")
print("Guess the word one letter at a time.")

while wrong_guesses < max_wrong_guesses:

    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    if "_" not in display:
        print("Congratulations! You won!")
        break

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")
        print("Wrong guesses:", wrong_guesses, "/", max_wrong_guesses)

if wrong_guesses == max_wrong_guesses:
    print("\nGame Over!")
    print("The word was:", word)
