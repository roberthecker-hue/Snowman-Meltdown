import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    random_index = random.randint(0, len(WORDS) - 1)
    secret_word = WORDS[random_index]
    return secret_word


def display_game_state(mistakes, secret_word, guessed_letters):
    """Displays the ASCII art for the current mistake count and the word with underscores."""
    current_stage = STAGES[mistakes]
    print(current_stage)

    displayed_letters = []
    for letter in secret_word:
        if letter in guessed_letters:
            displayed_letters.append(letter)
        else:
            displayed_letters.append("_")

    displayed_word = " ".join(displayed_letters)
    print("Word: " + displayed_word + "\n")


def is_word_guessed(secret_word, guessed_letters):
    """Checks if all letters of the secret word have been guessed."""
    for letter in secret_word:
        if letter not in guessed_letters:
            return False
    return True


def play_game():
    secret_word = get_random_word()
    print("Welcome to Snowman Meltdown!")
    print("Secret word selected: " + secret_word)  # For testing

    mistakes = 0
    max_mistakes = len(STAGES) - 1
    guessed_letters = []

    while mistakes < max_mistakes:
        display_game_state(mistakes, secret_word, guessed_letters)

        guess = input("Guess a letter: ").lower().strip()

        # Eingabe-Validierung: Genau 1 Buchstabe aus dem Alphabet
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter (a-z)!\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter!\n")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print(f"Your guess '{guess}' was correct!\n")
        else:
            mistakes = mistakes + 1
            print(f"Your guess '{guess}' was incorrect!\n")

        # Gewonnen-Prüfung
        if is_word_guessed(secret_word, guessed_letters):
            display_game_state(mistakes, secret_word, guessed_letters)
            print("Congratulations! You saved the snowman!\n")
            return

    # Verloren-Prüfung (Schneemann ist geschmolzen)
    display_game_state(mistakes, secret_word, guessed_letters)
    print(f"Game Over! The snowman melted. The word was: {secret_word}\n")


def main():
    """Wiederspiel-Schleife."""
    while True:
        play_game()
        play_again = (
            input("Do you want to play again? (yes/no): ").lower().strip()
        )
        if play_again not in ["yes", "y"]:
            print("Thanks for playing! Goodbye!")
            break


if __name__ == "__main__":
    main()
