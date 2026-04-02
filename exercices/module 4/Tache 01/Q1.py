while True:
    name = input("What is your name ?(8 to 12 characters): ")
    
    if 8 <= len(name) <= 12:
        print(f"Hello, {name}!")
        break
    print("The name must be between 8 and 12 characters long. Please Try Again !")