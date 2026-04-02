name = input("What is your name? ")

try:
    age_input = input("How old are you? ")
    age = int(age_input)
    print(f"{name}, in 5 years, you will be {age + 5} years old.")
except ValueError:
    print("Please write down a vaild age !")