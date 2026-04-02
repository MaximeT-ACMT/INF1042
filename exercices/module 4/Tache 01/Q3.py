try:
    a = float(input("Enter the first value (a): "))
    b = float(input("Enter the second value (b): "))

    product = a * b
    difference = a - b

    print(f"The Product is: {product}")
    print(f" The Difference is: {difference}")
except ValueError:
    print("Please write down vaild numbers !.")