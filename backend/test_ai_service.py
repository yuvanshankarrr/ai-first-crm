from app.services.ai_service import analyze_interaction


notes = """
Met Dr Rajesh Kumar.

Doctor appreciated Product X.

Requested clinical trial comparison.

Asked for follow-up next week.
"""

result = analyze_interaction(notes)

print("\n===== SUMMARY =====")
print(result["summary"])

print("\n===== NEXT ACTION =====")
print(result["next_action"])

print("\n===== FOLLOW-UP =====")
print(result["follow_up"])