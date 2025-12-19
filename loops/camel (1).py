def toSnakeCase(s):
    newString = ""
    for x in range(len(s)):
        if s[x].isupper():
            if x > 0:
                newString += "_"
            newString += s[x].lower()
        else:
            newString += s[x]
    return newString

userInput = input("CaseCamel :")
snakeCase = toSnakeCase(userInput)
print(snakeCase)
