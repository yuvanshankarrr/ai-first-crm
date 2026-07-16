from app.agents.crm_agent import crm_agent

notes = """
Met Dr Rajesh Kumar.

Doctor appreciated Product X.

Requested clinical trial comparison.

Asked for follow-up next week.
"""

print("=" * 50)
print("SUMMARY")
print("=" * 50)

result = crm_agent.invoke(
    {
        "task": "summarize",
        "notes": notes,
    }
)

print(result["summary"])


print("\n" + "=" * 50)
print("RECOMMEND")
print("=" * 50)

result = crm_agent.invoke(
    {
        "task": "recommend",
        "notes": notes,
    }
)

print(result["next_action"])


print("\n" + "=" * 50)
print("FOLLOW UP")
print("=" * 50)

result = crm_agent.invoke(
    {
        "task": "followup",
        "notes": notes,
    }
)

print(result["follow_up"])


print("\n" + "=" * 50)
print("EDIT")
print("=" * 50)

result = crm_agent.invoke(
    {
        "task": "edit",
        "notes": notes,
        "instruction": "Add that pricing discussion happened."
    }
)

print(result["updated_notes"])