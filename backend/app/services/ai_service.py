from app.agents.crm_agent import crm_agent


def analyze_interaction(notes: str) -> dict:

    result = crm_agent.invoke(
    {
        "task": "analyze",
        "notes": notes,
    }
        )

    return {
        "summary": result["summary"],
        "next_action": result["next_action"],
        "follow_up": result["follow_up"],
        }


def edit_notes(notes: str, instruction: str) -> str:

    result = crm_agent.invoke(
        {
            "task": "edit",
            "notes": notes,
            "instruction": instruction,
        }
    )

    return result["updated_notes"]




# from app.tools.summarize_notes import summarize_notes
# from app.tools.recommend_next_action import recommend_next_action
# from app.tools.extract_followup import extract_followup


# def analyze_interaction(notes: str) -> dict:
#     return {
#         "summary": summarize_notes(notes),
#         "next_action": recommend_next_action(notes),
#         "follow_up": extract_followup(notes),
#     }



# from app.agents.crm_agent import crm_agent


# def generate_summary(notes: str) -> str:
#     result = crm_agent.invoke(
#         {
#             "notes": notes
#         }
#     )

#     return result["summary"]