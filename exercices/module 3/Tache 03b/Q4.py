def string_operations():
    word = input("enter a word: ")
    print(word * 3)
    print(word + "!")
    if "a" in word:
        print("the letter a is in the word")
    else:
        print("the letter a is nowhere in the word")