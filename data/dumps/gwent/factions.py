import json
from pathlib import Path
from collections import defaultdict

# Input and output setup
input_file = "en.json"
output_dir = Path("faction_cards")
output_dir.mkdir(exist_ok=True)

# Load full JSON file
with open(input_file, "r", encoding="utf-8") as f:
    full_data = json.load(f)

# Extract the actual cards list
cards_raw = full_data["response"]

# Group cards by faction
faction_dict = defaultdict(list)
for card in cards_raw.values():
    faction = card["attributes"].get("faction", "Unknown")
    faction_dict[faction].append(card)

# Write each faction group to its own file
for faction, cards in faction_dict.items():
    safe_name = faction.replace(" ", "_") or "Unknown"
    output_path = output_dir / f"{safe_name}.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(cards, f, indent=2, ensure_ascii=False)

print(f"✅ Cards saved to '{output_dir}/' folder, split by faction.")

