import random

try:
    with open("high_score.txt", "r") as file:
        high_score = int(file.read())
except:
    high_score = float("inf")

target_number = random.randint(1, 100)
attempts = 0

print("I have picked a number between 1 and 100. Try to guess it!")
if high_score != float("inf"):
    print(f"Current high score: {high_score} attempts")

while True:

    guess = int(input("Enter your guess: "))
    attempts = attempts + 1

    if guess > target_number:
        print("Too high! Try a smaller number.")
    elif guess < target_number:
        print("Too low! Try a bigger number.")
    else:
        print(f"Correct! You guessed it in {attempts} attempts.")

        if attempts < high_score:
            print(f"New high score! Previous: {high_score} → New: {attempts}")
            with open("high_score.txt", "w") as file:
                file.write(str(attempts))

        break