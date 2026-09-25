# 高级版猜数字
import random

secret = random.randint(0, 100)
attempts = 0

print("The guess number games have begin!!!")

while True:
    user_input = input("Enter your guess: ")

    try:
        guess = int(user_input)
    except ValueError:
        print("Invalid input")
        continue

    if guess < 0 or guess> 100:
        print("Out of range,again.")
        continue

    attempts += 1

    if guess == secret:
        print("Congratulations, you guessed it!")
        print(f"You guessed {attempts} times.")
        break
    elif guess < secret:
        print("Your guess is too low.")
    else:
        print("Your guess is too high.")

print("Game Over!Thank you for your participation.!!!")