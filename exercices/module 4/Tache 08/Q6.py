import pandas as pd

df = pd.read_csv("nba_players.csv")

country_counts = df.groupby(["Team", "country"]).size()

print(country_counts)