from app.utils.llm import llm


def recommend_next_action(notes: str) -> str:

    prompt = f"""
You are an AI CRM assistant for pharmaceutical representatives.

Read these interaction notes.

Suggest exactly THREE actionable next steps.

Rules:
- Return only bullet points.
- No introduction.
- No explanation.
- Each bullet should be under 20 words.

Notes:

{notes}
"""

    response = llm.invoke(prompt)

    return response.content