import random

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def play_game():
    secret_word = get_random_word()
    print("Welcome to Snowman Meltdown!")
    print("Secret word selected: " + secret_word)  # for testing, later remove this line

    players_lives = 5

    while players_lives > 0:
        guess = input("Guess a letter: ").lower()
        if guess in secret_word:
            print(f"Your guess '{guess}' was correct! You still have {players_lives} live(s) left!")
        else:
            players_lives -= 1
            print(f"Your guess '{guess}' was incorrect! You lost 1 live.")
            print(f"You still have {players_lives} live(s) left!")


if __name__ == "__main__":
    play_game()
