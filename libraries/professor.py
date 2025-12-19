import random

def main():
    level = get_level()
    score = 0  # To keep track of the number of correct answers

    for _ in range(10):  # Generate 10 problems
        x = generate_integer(level)
        y = generate_integer(level)
        correct_answer = x + y
        attempts = 0  # Count the number of attempts for each question

        while attempts < 3:
            try:
                user_answer = input(f"{x} + {y} = ")
                user_answer = int(user_answer)  # Convert answer to an integer

                if user_answer == correct_answer:
                    score += 1
                    break  # Move to the next problem if the answer is correct
                else:
                    print("EEE")
                    attempts += 1

            except ValueError:
                print("EEE")  # Handle non-integer inputs
                attempts += 1

        if attempts == 3:
            print(f"{x} + {y} = {correct_answer}")  # Display the correct answer if the user fails

    print(f"Score: {score}/10")  # Final score

def get_level():
    while True:
        try:
            level = int(input("Enter the level (1, 2, or 3): "))
            if level in [1, 2, 3]:
                return level
            else:
                print("Invalid level. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def generate_integer(level):
    if level < 1 or level > 3:
        raise ValueError("Level must be between 1 and 3.")

    return random.randint(0, 10 ** level - 1)  # Generate a random integer with 'level' digits

if __name__ == "__main__":
    main()
