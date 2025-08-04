# look for value or variable in a word

word = "KHUSHI"
letter = input("Guess a letter")
if letter in word:
    print(f"letter is found {letter}")
else:
    print(f"{letter} not fount")
