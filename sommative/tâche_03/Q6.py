purchases = [
    ("Liam", "Galaxy Battle", "PC", 59.99),
    ("Emma", "Speed Zone", "PlayStation", 49.99),
    ("Liam", "Pixel Quest", "Switch", 39.99),
    ("Noah", "Galaxy Battle", "PC", 59.99),
    ("Emma", "Sky Builder", "PC", 29.99),
    ("Olivia", "Speed Zone", "Xbox", 54.99),
    ("Liam", "Sky Builder", "PC", 29.99),
    ("Noah", "Pixel Quest", "Switch", 39.99)
]

print("1. All purchases:")
for p in purchases:
    print(f"Customer: {p[0]}, Game: {p[1]}, Platform: {p[2]}, Price: {p[3]}")

# How many unique games were purchased?
unique_games = set()
unique_platforms = set()
for p in purchases:
    unique_games.add(p[1])
    unique_platforms.add(p[2])

total_spent = 0
customer_spending = {}
game_counts = {}

# PC purchases and spending summary
print("\n8. PC Purchases:")
for name, game, platform, price in purchases:
    total_spent += price
    

    if name in customer_spending:
        customer_spending[name] += price
    else:
        customer_spending[name] = price

    if game in game_counts:
        game_counts[game] += 1
    else:
        game_counts[game] = 1
        
    if platform == "PC":
        print(f"- {name} bought {game}")

top_customer = max(customer_spending, key=customer_spending.get)
top_game = max(game_counts, key=game_counts.get)

# Print final summary
print("\n--- FINAL SUMMARY ---")
print(f"Total purchases: {len(purchases)}")
print(f"Unique games: {len(unique_games)}")
print(f"Unique platforms: {unique_platforms}")
print(f"Biggest spender: {top_customer} ({customer_spending[top_customer]:.2f} $)")
print(f"Most popular game: {top_game}")