import random


def choose_word():
    words = ["python", "hangman", "challenge", "programming", "developer","teacher","programmer","student","motioncut"]
    return random.choice(words)


def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])


def hangman():
    word = choose_word()
    guessed_letters = set()
    incorrect_guesses = 6
    guessed_word = display_word(word, guessed_letters)

    print("Welcome to Hangman!")
    print(guessed_word)

    while incorrect_guesses > 0 and '_' in guessed_word:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            incorrect_guesses -= 1
            print(f"Wrong guess! You have {incorrect_guesses} incorrect guesses left.")

        guessed_word = display_word(word, guessed_letters)
        print(guessed_word)

    if '_' not in guessed_word:
        print(f"Congratulations! You've guessed the word '{word}' correctly!")
    else:
        print(f"Game over! The word was '{word}'.")


hangman()
