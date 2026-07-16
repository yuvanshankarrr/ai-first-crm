from app.agents.crm_agent import crm_agent


notes = """
Met Dr Rajesh Kumar.

Doctor appreciated Product X.

Requested clinical trial comparison.

Asked for follow-up next week.
"""

print("===== SUMMARIZE =====")

result = crm_agent.invoke(
    {
        "task": "summarize",
        "notes": notes,
    }
)

print(result["summary"])

print("\n=====================\n")

print("===== RECOMMEND =====")

result = crm_agent.invoke(
    {
        "task": "recommend",
        "notes": notes,
    }
)

print(result["next_action"])