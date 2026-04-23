import pandas as pd

df = pd.read_csv("nba_players.csv")

low_scorers = df[df['ppg'] < 5]

low_scorers.to_csv("low_scorers.csv", index=False)