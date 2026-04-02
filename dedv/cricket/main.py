import json
import csv
import os

matches = []
deliveries = []

folder_path = "matches_json"

for file in os.listdir(folder_path):
    if file.endswith(".json"):
        match_id = file.replace(".json", "")
        
        with open(os.path.join(folder_path, file), "r") as f:
            data = json.load(f)

        info = data["info"]

        # MATCH TABLE
        matches.append([
            match_id,
            info["teams"][0],
            info["teams"][1],
            info.get("venue", ""),
            info.get("city", ""),
            info["dates"][0]
        ])

        # DELIVERY TABLE
        for inning_index, inning in enumerate(data["innings"]):
            for over in inning["overs"]:
                for ball_index, delivery in enumerate(over["deliveries"]):

                    deliveries.append([
                        match_id,
                        inning_index + 1,
                        over["over"],
                        ball_index + 1,
                        delivery["batter"],
                        delivery["bowler"],
                        delivery["runs"]["batter"],
                        1 if "wickets" in delivery else 0
                    ])

# SAVE MATCHES
with open("matches.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["match_id","team1","team2","venue","city","date"])
    writer.writerows(matches)

# SAVE DELIVERIES
with open("deliveries.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["match_id","inning","over","ball","batter","bowler","runs","wicket"])
    writer.writerows(deliveries)

print("DONE ✅ CSV CREATED")