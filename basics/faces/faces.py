def main():
    emoji_output = convert()
    print(emoji_output)


def convert():
    emoticons = input("Enter any sentence:")
    emoticons = emoticons.replace(":)","🙂").replace(":(","🙁")
    return emoticons

main()
