import random

stages = [
"""
   -----
   |   |
   |
   |
   |
   |
---------
""",
"""
   -----
   |   |
   |   O
   |
   |
   |
---------
""",
"""
   -----
   |   |
   |   O
   |   |
   |
   |
---------
""",
"""
   -----
   |   |
   |   O
   |  /|
   |
   |
---------
""",
"""
   -----
   |   |
   |   O
   |  /|\\
   |
   |
---------
""",
"""
   -----
   |   |
   |   O
   |  /|\\
   |  /
   |
---------
""",
"""
   -----
   |   |
   |   O
   |  /|\\
   |  / \\
   |
---------
"""
]

words = ["apple", "banana", "grape", "mango", "orange"]
word = random.choice(words)

guessed = ["_"] * len(word)
attempts = 6
used_letters = []

print("Welcome to Hangman Game")
print("Word:", " ".join(guessed))

while attempts > 0:
    print(stages[6 - attempts])
    letter = input("Enter a letter: ").lower()

    if letter in used_letters:
        print("You already guessed this letter!")
        continue

    used_letters.append(letter)

    if letter in word:
        print("Correct guess!")
        for i in range(len(word)):
            if word[i] == letter:
                guessed[i] = letter
    else:
        attempts -= 1
        print("Wrong guess! Attempts left:", attempts)

    print("Word:", " ".join(guessed))

    if "_" not in guessed:
        print("\nCongratulations! You won!")
        break

if "_" in guessed:
    print(stages[6])
    print("\nGame Over! You lost.")
    print("The word was:", word)
