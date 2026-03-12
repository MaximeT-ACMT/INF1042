grades = []

while True:
    print("Menu")
    print("1. grades")
    print("2. Average")
    print("3. passes")
    print("4. fails")
    print("5. Quit")

    choice = input("Choose your number 1 - 5: ")

    if choice == "1":
        n = int(input("Number of grades? "))
        for i in range(n):
            grade = int(input("Grade: "))
            grades(grade)

    elif choice == "2":
        if grades == []:
            print("Grades not recieved")
        else:
            total = 0
            count = 0
            for g in grades:
                total = total + g
                count = count + 1
            print("Average:", total // count)  

    elif choice == "3":
        passes = 0
        for g in grades:
            if g >= 50:
                passes
        print("Passes:", passes)

    elif choice == "4":
        fails = 0
        for g in grades:
            if g < 50:
                fails
        print("Fails:")

    elif choice == "5":
        print
        break