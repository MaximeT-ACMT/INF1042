try:
    user_input = input("Enter your age: ")
    if not user_input.isdigit():
        raise ValueError("age must be a whole number.")
    
    age = int(user_input)
    print(f"You are {age} years old.")

except ValueError as e:
    print(f"Error: {e}")