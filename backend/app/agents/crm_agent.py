from langgraph.graph import StateGraph, START, END
from typing import TypedDict

from app.utils.llm import llm


class CRMState(TypedDict):
    notes: str
    summary: str


def summarize_node(state: CRMState):
    response = llm.invoke(
        f"""
        You are an AI CRM assistant for pharmaceutical sales representatives.

        Summarize the following doctor interaction.

        Rules:
        - Return ONLY 3 bullet points.
        - Do not add introductions like "Here are..."
        - Do not add conclusions.
        - Keep each bullet under 20 words.
        - Focus on doctor interest, requests, and follow-up.

        Notes:
        {state["notes"]}
        """
    #     f"""
    #     Summarize this doctor's visit in 3 concise bullet points.

    #     Notes:
    #     {state['notes']}
    #
    #      """
     )


    return {
        "summary": response.content
    }


graph = StateGraph(CRMState)

graph.add_node("summarize", summarize_node)

graph.add_edge(START, "summarize")
graph.add_edge("summarize", END)

crm_agent = graph.compile()