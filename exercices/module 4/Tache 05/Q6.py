
matches = (
    ("Tigers", "Lynx", 25, 18),
    ("Eagles", "Panthers", 22, 25),
    ("Tigers", "Panthers", 25, 23),
    ("Lynx", "Eagles", 19, 25),
    ("Tigers", "Eagles", 21, 25),
    ("Lynx", "Panthers", 25, 20)
)

wins = {}
total_points = {}
losses = {}

for team1, team2, score1, score2 in matches:

    for team in [team1, team2]:
        wins.setdefault(team, 0)
        losses.setdefault(team, 0)
        total_points.setdefault(team, 0)

    total_points[team1] += score1
    total_points[team2] += score2

    if score1 > score2:
        wins[team1] += 1
        losses[team2] += 1
        print(f"The {team1} beat the {team2} by {score1} to {score2}.")
    else:
        wins[team2] += 1
        losses[team1] += 1
        print(f"The {team2} beat the {team1} by {score2} to {score1}.")

print("\n--- TOURNAMENT SUMMARY ---")

for team in wins:
    w = wins[team]
    l = losses[team]
    pts = total_points[team]
    
    if w > l:
        record = "more wins than losses"
    elif w < l:
        record = "more losses than wins"
    else:
        record = "even record (wins = losses)"
        
    print(f"{team}: {w} wins, {pts} total points. Finished with {record}.")

most_wins = max(wins, key=wins.get)
most_points = max(total_points, key=total_points.get)

print(f"\nTeam with most wins: {most_wins}")
print(f"Team with most points: {most_points}")