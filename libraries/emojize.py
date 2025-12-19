import emoji

def main():

    user_input = input("Enter a string with emoji codes: ")

    emojize_string = emoji.emojize(user_input, language ='alias')

    print(emojize_string)

if __name__ == "__main__":
    main()
