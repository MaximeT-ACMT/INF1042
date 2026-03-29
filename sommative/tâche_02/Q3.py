# Maxime Talbot
# Calculate a discount and tax for a purchase based on the total price.

price = float(input("Please enter the purchase price: "))
tax_rate = 0.13

if (price < 50):
    discount_percent = 0
elif (50 <= price <= 100):
    discount_percent = 0.10
else:
    discount_percent = 0.15

discount_amount = price * discount_percent
subtotal = price - discount_amount
tax_amount = subtotal * tax_rate
total = subtotal + tax_amount

print(f"Original Price: ${price:.2f}")
print(f"Discount: {discount_percent * 100}% (${discount_amount:.2f})")
print(f"Subtotal after discount: ${subtotal:.2f}")
print(f"Tax: ${tax_amount:.2f}")
print(f"Total to pay: ${total:.2f}")

# Line 4 tell us to write the purchase price of the item
# Line 7 to 12 calculate what discount applies
# Line 14 to 17 tells us how much is discounted, subtotal, tax amount and your final total
# Line 19 to 23 Prints all of the information