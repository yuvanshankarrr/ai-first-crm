from app.utils.llm import llm


def summarize_notes(notes: str) -> str:
    prompt = f"""
You are an AI CRM assistant for pharmaceutical representatives.

Summarize the following doctor interaction.

Rules:
- Return ONLY 3 bullet points.
- No introduction.
- No conclusion.
- Each bullet should be concise.
- Focus on doctor's interest, requests, and follow-up.

Notes:

{notes}
"""

    response = llm.invoke(prompt)

    return response.content