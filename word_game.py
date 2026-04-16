import csv
import random
import os


def select_word(filename):
    """
    read from a csv and pick a random word from a list of five letter words
    parameters: filename
    return: word

    """
    word_list = []

    with open(filename, "rt") as word_file:
        reader = csv.reader(word_file)
        next(reader)
        for row in reader:
            word_list.append(row[0])

    rand_word = random.choice(word_list)

    return rand_word


def user_guess():
    """
    ask user for a guess, word must be five letters and must be a string
    parameters: none
    return: guess

    """

    while True:
        print()
        guess = input("Try to guess the word (must be 5 letters): ").upper()
        print()

        if len(guess) != 5:
            print("Guess must be exactly 5 letters.")
        elif not guess.isalpha():
            print("Guess must only contain letters.")
        else:
            return guess


def check_guess(secret_word, guess):
    """
    compares the secret word to the user guess and displays whether there is
    a letter in the correct position, wrong position or not in the secret word
    parameters: secret_word, guess
    returns: check_letter

    """
    result = [""] * 5
    secret_copy = list(secret_word)

    for i in range(5):
        if guess[i] == secret_word[i]:
            result[i] = "G"
            secret_copy[i] = None

    for i in range(5):
        if result[i] == "":
            if guess[i] in secret_copy:
                result[i] = "Y"
                secret_copy[secret_copy.index(guess[i])] = None
            else:
                result[i] = "_"

    return result


def print_grid(guesses, attempt):

    os.system("cls" if os.name == "nt" else "clear")

    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"

    print("-" * 21)
    title = "WORD GAME"
    print(title.center(21))
    print("-" * 21)
    print(f"Attempt {attempt + 1} / 6")
    print()

    for guess, result in guesses:
        row = []

        for i in range(5):
            if result[i] == "G":
                row.append(GREEN + guess[i] + RESET)
            elif result[i] == "Y":
                row.append(YELLOW + guess[i] + RESET)
            else:
                row.append("_")

        print(" ".join(row))
        print()

    for _ in range(6 - len(guesses)):
        print("_ _ _ _ _")
        print()


def main():

    GREEN = "\033[92m"
    RED = "\033[91m"
    RESET = "\033[0m"

    while True:
        secret_word = select_word("words.csv").upper()
        guesses = []

        for attempt in range(6):
            print_grid(guesses, attempt)

            guess = user_guess()
            result = check_guess(secret_word, guess)

            guesses.append((guess, result))

            if result == ["G"] * 5:
                print_grid(guesses, attempt)
                print(GREEN + "You win!" + RESET)
                break

        else:
            print_grid(guesses, 5)
            print(RED + "You lost." + RESET, "Word was:", GREEN + secret_word + RESET)

        print()

        play_again = input("Play again? (y/n): ").lower()

        if play_again != "y":
            break


if __name__ == "__main__":
    main()
