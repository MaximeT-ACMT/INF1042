import random
import string
from datetime import date

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
birth_year = int(input("Enter your birth year (YYYY): "))
city = input("Enter your city: ")

username = first_name.lower() + "." + last_name.lower()
full_id = username + "@" + city.lower() + ".ca"

current_year = date.today().year
age = current_year - birth_year
is_adult = (age >= 18)

part1 = first_name[:2]
part2 = last_name[-2:]

random = "".join(random.choices(string.ascii_letters + string.digits, k=4))

password = part1 + part2 + str(birth_year) + random

print("\n--- Account Details ---")
print("Username: " + username)
print("Full ID: " + full_id)
print("Adult (18+): " + str(is_adult))
print("Generated Password: " + password)