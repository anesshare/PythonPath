import random

words = ("apple", "watermelon", "orange", "banana", "coconut")

hangmanArt = {
    0: (
        "  +---+",
        "  |   |",
        "      |",
        "      |",
        "      |",
        "      |",
        "========="
    ),
    1: (
        "  +---+",
        "  |   |",
        "  O   |",
        "      |",
        "      |",
        "      |",
        "========="
    ),
    2: (
        "  +---+",
        "  |   |",
        "  O   |",
        "  |   |",
        "      |",
        "      |",
        "========="
    ),
    3: (
        "  +---+",
        "  |   |",
        "  O   |",
        " /|   |",
        "      |",
        "      |",
        "========="
    ),
    4: (
        "  +---+",
        "  |   |",
        "  O   |",
        " /|\\  |",
        "      |",
        "      |",
        "========="
    ),
    5: (
        "  +---+",
        "  |   |",
        "  O   |",
        " /|\\  |",
        " /    |",
        "      |",
        "========="
    ),
    6: (
        "  +---+",
        "  |   |",
        "  O   |",
        " /|\\  |",
        " / \\  |",
        "      |",
        "========="
    )
}

def displayMan(wrongGuesses):
    for line in hangmanArt[wrongGuesses]:
        print(line)

def displayHint(hint):
    print(" ".join(hint))
    print()  # dodao prazan red radi preglednosti

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrongGuesses = 0
    guessedLetters = set()
    isRunning = True

    while isRunning:
        displayMan(wrongGuesses)
        displayHint(hint)
        guess = input("Enter a letter: ").lower()

        # validacija
        if not guess.isalpha() or len(guess) != 1:
            print("⚠️ Enter a single letter.")
            continue

        if guess in guessedLetters:
            print("Already guessed that letter.")
            continue

        guessedLetters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrongGuesses += 1

        if "_" not in hint:
            print("🎉 You won!")
            displayHint(hint)
            isRunning = False
        elif wrongGuesses >= 6:
            print("💀 You lost!")
            displayMan(wrongGuesses)
            print(f"The word was: {answer}")
            isRunning = False

if __name__ == "__main__":
    main()
