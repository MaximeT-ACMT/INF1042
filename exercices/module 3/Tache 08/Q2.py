Number = int(input("Enter a number: "))

X3 = Number - (Number // 3) * 3
X5 = Number - (Number // 5) * 5

if X3 == 0 and X5 == 0:
    print("It can divide by 3 and 5")
elif X3 == 0:
    print("It can divide by 3")
elif X5 == 0:
    print("It can divide by 5")
else:
    print("Can't divide by 3 or 5")