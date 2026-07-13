from app.utils.llm import llm


def edit_interaction(
    original_notes: str,
    instruction: str,
) -> str:

    prompt = f"""
You are an AI CRM assistant.

Below are the existing interaction notes.

Your job is to update them based on the user's instruction.

Rules:
- Preserve existing information unless instructed otherwise.
- Apply the requested changes.
- Return ONLY the updated notes.
- Do not explain what you changed.

Original Notes:

{original_notes}

Instruction:

{instruction}
"""

    response = llm.invoke(prompt)

    return response.content