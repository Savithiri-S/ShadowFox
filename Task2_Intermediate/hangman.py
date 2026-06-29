import random

word_hints = {
    "programming": "Writing instructions for computers",
    "python": "Popular programming language",
    "gaming": "Playing video games",
    "computer": "Electronic machine",
    "guessing": "Trying to find the answer",
    "internet": "Global network",
    "keyboard": "Used for typing",
    "monitor": "Displays computer output",
    "software": "Programs running on a computer",
    "developer": "Person who writes code"
}

secret_word = random.choice(list(word_hints.keys()))

guessed_letters = []
lives = 6

stages = [
"""
 -----
 |   |
 |   O
 |  /|\\
 |  / \\
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
 |
 |
 |
---------
""",
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
 
 
 
 
 
 
---------
"""
]

print("🎮 Welcome to Hangman!")
print("Hint:", word_hints[secret_word])

while lives > 0:

    print(stages[lives])

    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    if "_" not in display_word:
        print("\n🎉 Congratulations! You won!")
        break

    guess = input("\nEnter a letter: ").lower()
    
    # Validate input
    
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue
    
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("✅ Correct!")
    else:
        print("❌ Wrong!")
        lives -= 1

if lives == 0:
    print(stages[0])
    print("\n💀 Game Over!")
    print("The word was:", secret_word)