import random
import time

num_questions = int(input("How many math questions would you like to solve? "))
correct_count = 0
incorrect_count = 0
total_time = 0
operations = ["+", "-", "*", "/"]

for i in range(num_questions):
    num1 = random.randint(1, 9)
    num2 = random.randint(1, 9)
    op = random.choice(operations)

    if (op == "+"):
        real_answer = num1 + num2
    elif (op == "-"):
        real_answer = num1 - num2
    elif (op == "*"):
        real_answer = num1 * num2
    elif (op == "/"):
        real_answer = round(num1 / num2, 2)

    start_clock = time.time()
    print("Question " + str(i + 1) + ": " + str(num1) + " " + op + " " + str(num2) + " = ?")
    user_answer = float(input("Your answer: "))
    end_clock = time.time()
    
    duration = round(end_clock - start_clock, 2)
    total_time = total_time + duration

    if (user_answer == real_answer):
        print("Correct! (Time: " + str(duration) + "s)")
        correct_count = correct_count + 1
    else:
        print("Wrong. The answer was " + str(real_answer) + ". (Time: " + str(duration) + "s)")
        incorrect_count = incorrect_count + 1

print("\n--- Final Results ---")
print("Total Correct: " + str(correct_count))
print("Total Incorrect: " + str(incorrect_count))
print("Total Time Taken: " + str(round(total_time, 2)) + " seconds")