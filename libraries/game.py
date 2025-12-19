import random

while True:
    try:
        Level = int(input("Level:"))
        if Level < 0:
            continue

        guess = random.randint(1, Level)

    except ValueError:

        continue

    if guess == Level:
        print(f"Guess: {guess}")
        print("Just right!")
        break

    elif guess < Level:
        print(f"Guess: {guess}")
        print("Too small!")

    else:
        print(f"Guess: {guess}")
        print("Too large!")
