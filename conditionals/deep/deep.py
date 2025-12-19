def main():
    Question_of_Life = condition(input("What is the answer to the Great Question of, the Universe, and Everything ? "))

    if  Question_of_Life == "42":
        print("Yes")

    elif Question_of_Life == "Forty Two":
        print("Yes")

    elif Question_of_Life == "forty-two" or Question_of_Life =="forty two":
        print("Yes")


    else:
        print("No")

def condition(question):
    question = question.strip().lower()
    return question

main()
