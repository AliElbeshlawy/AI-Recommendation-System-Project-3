def recommend(items, preferences):
    results = []

    for item in items:
        score = 0

        for tag in item["tags"]:
            if tag in preferences:
                score += 1

        results.append({
            "name": item["name"],
            "score": score
        })

    results.sort(key=lambda x: x["score"], reverse=True)

    return results