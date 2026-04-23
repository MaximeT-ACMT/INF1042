import pandas as pd

df = pd.read_csv("nba_players.csv")

top_salary = df.sort_values("salary", ascending=False).head(10)

print(top_salary[["Basketball Team", "salary"]])