def remove_vowels():
    text = input("Input :")
    vowels = ['a','A','e','E','i','I','E','o','O','u','U']
    results = ""

    for char in text:
        if char not in vowels:
            results = results + char
    print(f"Output :{results}")
remove_vowels()
