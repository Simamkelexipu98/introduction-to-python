def format_names(names):

    num_names = len(names)

    if num_names == 1:
        return f"Adieu, adieu, to {names[0]}."
    elif num_names == 2:
        return f"Adieu, adieu ,to {names[0]} and {names[1]}."
    else:

        return f"Adieu, adieu, to {', '.join(names[:-1])}, and {names[-1]}."

def main():
    names = []
    try:
        while True:
            name = input()
            names.append(name)
    except EOFError:

        pass


    farewell_message = format_names(names)
    print(farewell_message)

if __name__ == "__main__":
    main()
