from typing import TypedDict
from langgraph.graph import StateGraph, END

from app.tools.outreach_tools import portfolio_response


#  Proper state typing
class AgentState(TypedDict):
    message: str
    response: str


def agent_node(state: AgentState) -> AgentState:

    message = state["message"].lower()

    if "portfolio" in message:
        return {
            "message": state["message"],
            "response": portfolio_response()["message"],
        }

    return {
        "message": state["message"],
        "response": "LangGraph agent processed your request.",
    }


def build_graph():

    graph = StateGraph(AgentState)

    graph.add_node("agent", agent_node)

    graph.set_entry_point("agent")
    graph.add_edge("agent", END)

    return graph.compile()


langgraph_agent = build_graph()
