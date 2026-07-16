from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Optional

# from app.utils.llm import llm
from app.tools.summarize_notes import summarize_notes
from app.tools.recommend_next_action import recommend_next_action

from app.tools.extract_followup import extract_followup
from app.tools.edit_interaction import edit_interaction



class CRMState(TypedDict):
    task: str

    notes: str

    instruction: Optional[str]

    summary: Optional[str]

    next_action: Optional[str]

    follow_up: Optional[str]

    updated_notes: Optional[str]


def summarize_node(state: CRMState):

    return {
        "summary": summarize_notes(
            state["notes"]
        )
    }


def recommend_node(state: CRMState):

    return {
        "next_action": recommend_next_action(
            state["notes"]
        )
    }

def followup_node(state: CRMState):

    return {
        "follow_up": extract_followup(
            state["notes"]
        )
    }

def edit_node(state: CRMState):

    return {
        "updated_notes": edit_interaction(
            state["notes"],
            state["instruction"]
        )
    }


def analyze_node(state: CRMState):

    summary = summarize_notes(state["notes"])

    next_action = recommend_next_action(state["notes"])

    follow_up = extract_followup(state["notes"])

    return {
        "summary": summary,
        "next_action": next_action,
        "follow_up": follow_up,
    }


def decide_route(state: CRMState):

    task = state["task"].lower()

    if task =="analyze":
        return "analyze"

    if task == "summarize":
        return "summarize"

    if task == "recommend":
        return "recommend"
    
    if task == "followup":
        return "followup"
    
    if task == "edit":
        return "edit"

    return "summarize"


graph = StateGraph(CRMState)

graph.add_node("summarize", summarize_node)
graph.add_node("recommend", recommend_node)
graph.add_node("followup", followup_node)
graph.add_node("edit", edit_node)
graph.add_node("analyze", analyze_node)


# graph.add_edge(START, "summarize")
# graph.add_edge("summarize", END)

graph.add_conditional_edges(
    START,
    decide_route,
    {
        "analyze": "analyze",
        "summarize": "summarize",
        "recommend": "recommend",
        "followup": "followup",
        "edit": "edit",
    },
)

graph.add_edge("summarize", END)
graph.add_edge("recommend", END)
graph.add_edge("followup", END)
graph.add_edge("edit", END)
graph.add_edge("analyze", END)

crm_agent = graph.compile()