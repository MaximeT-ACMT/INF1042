try:
    n1 = input("Grade 1: ")
    n2 = input("Grade 2: ")
    
    try:
        grade1 = float(n1)
        grade2 = float(n2)
    except ValueError:
        raise ValueError("grades must be numerical.")

    if not (0 <= grade1 <= 100 and 0 <= grade2 <= 100):
        raise ValueError("grades must be between 0 and 100.")

except ValueError as e:
    print(f"Error: {e}")

else:
    average = (grade1 + grade2) / 2
    print(f"Average: {average}")

finally:
    print("End of program.")