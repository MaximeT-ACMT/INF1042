balance = 250.00

try:
    user_input = input("Amount to withdraw: ").replace('$', '')
    
    try:
        amount = float(user_input)
    except ValueError:
        raise ValueError("invalid numerical format.")

    if amount <= 0:
        raise ValueError("amount must be greater than zero.")
    
    if amount > balance:
        raise ValueError("insufficient funds.")

except ValueError as e:
    print(f"Error: {e}")

else:
    balance -= amount
    print("Withdrawal accepted.")
    print(f"New balance: {balance:.2f} $")

finally:
    print("End of transaction.")