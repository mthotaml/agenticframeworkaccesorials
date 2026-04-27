def recommend(data):
    score = 0
    suggestions = []
    evidence = []

    if data["location_type"] == "hospital":
        score += 0.4
        evidence.append("Hospital location")

    if not data["has_loading_dock"]:
        score += 0.3
        evidence.append("No loading dock")

    if not data["has_forklift"]:
        score += 0.2
        evidence.append("No forklift")

    if score > 0.5:
        suggestions.append("Liftgate")

    if data["location_type"] in ["hospital", "school"]:
        suggestions.append("Limited Access")

    confidence = min(score, 1.0)

    return {
        "suggestions": suggestions,
        "confidence": confidence,
        "explanation": "Signals indicate special handling requirements",
        "evidence": evidence,
        "rollout_action": "auto_apply" if confidence > 0.8 else "review"
    }
