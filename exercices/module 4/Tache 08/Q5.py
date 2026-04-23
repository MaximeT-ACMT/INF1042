import pandas as pd

df = pd.read_csv("nba_players.csv")

salary_stats = df.groupby("position")["salary"].agg(["mean", "max", "min"]).round(1)

print(salary_stats)