import random
import time

print("🎮 Welcome to the Ultimate Number Guessing Game! 🎮\n")

# Game settings
LOWER = 1
UPPER = 100
MAX_ATTEMPTS = 7

secret_number = random.randint(LOWER, UPPER)
attempts = 0

print(f"I'm thinking of a number between {LOWER} and {UPPER}.")
print(f"You have {MAX_ATTEMPTS} attempts to guess it. Good luck!\n")

# Fun delay
time.sleep(1)

while attempts < MAX_ATTEMPTS:
    try:
        guess = int(input(f"Attempt {attempts + 1}: Enter your guess: "))
    except ValueError:
        print("⚠️ Please enter a valid number!\n")
        continue

    attempts += 1

    if guess < secret_number:
        print("📉 Too low! Try a higher number.\n")
    elif guess > secret_number:
        print("📈 Too high! Try a lower number.\n")
    else:
        print(f"🎉 BOOM! You guessed it in {attempts} attempts!")
        break

    # Hint system
    if attempts == 4:
        if secret_number % 2 == 0:
            print("💡 Hint: The number is EVEN!\n")
        else:
            print("💡 Hint: The number is ODD!\n")

# Game over
if guess != secret_number:
    print(f"💀 Game Over! The number was {secret_number}.")

# Replay option
play_again = input("\nDo you want to play again? (yes/no): ").lower()
if play_again == "yes":
    print("\nRestart the script to play again! 🔁")
else:
    print("Thanks for playing! 👋")