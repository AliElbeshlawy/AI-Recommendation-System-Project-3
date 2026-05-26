import data

items = data.items
from recommender import recommend

print("🎯 AI Recommendation System")
print("---------------------------")

user_input = input("Enter your interests (comma separated): ")

preferences = [x.strip().lower() for x in user_input.split(",")]

results = recommend(items, preferences)

print("\n📌 Recommendations:\n")

found = False

for r in results:
   if r["score"] >= 1:
        print(f"{r['name']} -> Score: {r['score']}")
        found = True

if not found:
    print("No matches found. Try different interests.")