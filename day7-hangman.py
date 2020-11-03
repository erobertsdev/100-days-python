import random

word_list = ["aardvark", "baboon", "camel", "dolphin", "beaver", "elephant", "platypus"]
word = random.choice(word_list)
display = []

# create blank word display
for char in word:
    display += '_'
print(display)

# the game
guess_count = 0
lives = 6
while "_" in display and lives != 0:
    guess = input("Guess a letter: ").lower()

    if guess not in display:
        if guess not in word:
            lives -= 1

        for idx, letter in enumerate(word):
            if guess == letter:
                display[idx] = guess

        print(display)
        print(f"You have {lives} guesses remaining.")
    else:
        print(f"You already guessed {guess}, try again.")
        print(f"You have {lives} guesses remaining.")

# game over messages
if lives > 0:
    print("You win!")
else:
    print(f"You lose! The word was '{word}'.")
