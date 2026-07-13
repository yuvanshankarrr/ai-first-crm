from app.utils.llm import llm


def extract_followup(notes: str) -> str:
    prompt = f"""
You are an AI assistant.

Read these doctor's visit notes.

Extract ONLY the follow-up date or timeframe.

Examples:

Next week
Tomorrow
2026-07-20
After 2 weeks

If no follow-up exists, return:

None

Notes:

{notes}
"""

    response = llm.invoke(prompt)

    return response.content.strip()