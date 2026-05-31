target_number = 18

print("--- Welcome to the Number Guessing Game! ---")
print("Type '0' if you want to quit the game.\n")

while True:
    # Get the user's guess
    guess = int(input("Enter your guess: "))

    # Check if the user wants to quit
    if guess == 0:
        print("Thanks for playing! Goodbye.")
        break # This exits the loop immediately

    # Checking the guess
    if guess > target_number:
        print("Guess less! 👇\n")
    elif guess < target_number:
        print("Guess More! ☝️\n")
    else:
        print("🎉 That's the correct one! You win! 🎉")
        break  # Exit the loop since they won