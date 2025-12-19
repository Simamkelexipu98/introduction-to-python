# Get a an input from the user
#if a user enters Hello or hello then the output should be $0 : Cindition 1
# if a user enters Hello followed by something the output should be $0 : Condition 2
#if a user enters a name that starts with "H" but not hello the output should be $20 : Condition 3
#if a user enters a name that does not include "hello" or that does not start with "Hello" output should be $100 : Condition 4

def main():
    # Prompt the user for a greeting
    greeting = input("Enter your greeting: ")
    # Get the result based on the conditions
    result = determine_reward(greeting)
    # Print the result
    print(result)

def determine_reward(greeting):
    # Ignore leading whitespace and convert to lowercase
    greeting = greeting.strip().lower()

    # Check if the greeting starts with "hello"
    if greeting.startswith("hello"):
        return "$0"
    # Check if the greeting starts with "h" but is not "hello"
    elif greeting.startswith("h"):
        return "$20"
    # Any other greeting
    else:
        return "$100"
if __name__ == "__main__":
    main()
