import pandas as pd
import matplotlib.pyplot as plt

# LOAD DATA
matches = pd.read_csv("matches.csv")
deliveries = pd.read_csv("deliveries.csv")

# TAKE SMALL SAMPLE
d = deliveries.head(100)

# -----------------------------
# 📊 1. Runs vs Ball
# -----------------------------
plt.figure()
plt.plot(d["ball"], d["runs"])
plt.title("Runs vs Ball")
plt.xlabel("Ball")
plt.ylabel("Runs")
plt.show()

# -----------------------------
# 📊 2. Runs per Over
# -----------------------------
runs_per_over = d.groupby("over")["runs"].sum()

plt.figure()
runs_per_over.plot(kind='bar')
plt.title("Runs per Over")
plt.xlabel("Over")
plt.ylabel("Total Runs")
plt.show()

# -----------------------------
# 📊 3. Wickets per Over
# -----------------------------
wickets_per_over = d.groupby("over")["wicket"].sum()

plt.figure()
wickets_per_over.plot(kind='bar')
plt.title("Wickets per Over")
plt.xlabel("Over")
plt.ylabel("Wickets")
plt.show()

# -----------------------------
# 📊 4. Top Batters
# -----------------------------
top_batters = d["batter"].value_counts().head(5)

plt.figure()
top_batters.plot(kind='bar')
plt.title("Top Batters (Sample)")
plt.xlabel("Batter")
plt.ylabel("Balls Played")
plt.xticks(rotation=45)
plt.show()

# -----------------------------
# 📊 5. Top Bowlers
# -----------------------------
top_bowlers = d["bowler"].value_counts().head(5)

plt.figure()
top_bowlers.plot(kind='bar')
plt.title("Top Bowlers (Sample)")
plt.xlabel("Bowler")
plt.ylabel("Balls Bowled")
plt.xticks(rotation=45)
plt.show()

# -----------------------------
# 📊 6. Matches per Team
# -----------------------------
team_counts = matches["team1"].value_counts().head(5)

plt.figure()
team_counts.plot(kind='bar')
plt.title("Matches per Team")
plt.xlabel("Team")
plt.ylabel("Matches")
plt.xticks(rotation=45)
plt.show()

# -----------------------------
# 📊 7. Matches per Venue
# -----------------------------
venue_counts = matches["venue"].value_counts().head(5)

plt.figure()
venue_counts.plot(kind='bar')
plt.title("Matches per Venue")
plt.xlabel("Venue")
plt.ylabel("Matches")
plt.xticks(rotation=45)
plt.show()