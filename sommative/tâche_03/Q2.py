# Create the tuple for the product
product1 = ("Keyboard", 49.99, 12)

# print the tuples elements
print("2. Values:", product1[0], "|", product1[1], "|", product1[2])

# seperating parts of the tuple
name, price, quantity = product1

print(f"4. The product {name} costs {price} $ and there are {quantity} in stock.")

product2 = ("Mouse", 25.50, 20)

# Comparing prices of the two products
if product1[1] > product2[1]:
    print(f"5. The more expensive product is: {product1[0]}")
else:
    print(f"5. The more expensive product is: {product2[0]}")