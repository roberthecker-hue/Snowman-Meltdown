import random

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

# Snowman ASCII Art stages
STAGES = [
    # Stage 0: Full snowman
    """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     ( : ) 
     """,
    # Stage 1: Bottom part starts melting
    """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     """,
    # Stage 2: Only the head remains
    """
      ___  
     /___\\ 
     (o o) 
     """,
    # Stage 3: Snowman completely melted
    """
      ___  
     /___\\ 
     """,
]


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


def play_game():
    secret_word = get_random_word()
    print("Welcome to Snowman Meltdown!")
    print(
        "Secret word selected: " + secret_word
    )  # for testing, later remove this line

    mistakes = 0
    guessed_letters = []

    # Deine While-Schleife, kombiniert mit der Anzeige:
    while mistakes < len(STAGES) - 1:
        display_game_state(mistakes, secret_word, guessed_letters)

        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter!\n")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print(f"Your guess '{guess}' was correct!\n")
        else:
            mistakes = mistakes + 1
            print(f"Your guess '{guess}' was incorrect!\n")

    # Am Ende noch den geschmolzenen Zustand zeigen:
    display_game_state(mistakes, secret_word, guessed_letters)
    print("Game Over! The word was: " + secret_word)


if __name__ == "__main__":
    play_game()
