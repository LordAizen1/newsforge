import os
from dotenv import load_dotenv

load_dotenv()  # must run before node imports so env vars are set at module init

from langgraph.graph import StateGraph, START, END
from agent.state import DigestState
from agent.nodes import search
from agent.nodes import filter_news
from agent.nodes import categorize
from agent.nodes import summarize
from agent.nodes import format_digest
from agent.nodes import mail
from agent.nodes import whatsapp


def route_delivery(state: DigestState):
    channel = os.getenv("DELIVERY_CHANNEL", "email")
    if channel == "both":
        return ["send_email", "send_whatsapp"]
    if channel == "whatsapp":
        return "send_whatsapp"
    return "send_email"


def build_graph():
    graph = StateGraph(DigestState)

    graph.add_node("search",        search.run)
    graph.add_node("filter",        filter_news.run)
    graph.add_node("categorize",    categorize.run)
    graph.add_node("summarize",     summarize.run)
    graph.add_node("format",        format_digest.run)
    graph.add_node("send_email",    mail.run)
    graph.add_node("send_whatsapp", whatsapp.run)

    graph.add_edge(START,          "search")
    graph.add_edge("search",       "filter")
    graph.add_edge("filter",       "categorize")
    graph.add_edge("categorize",   "summarize")
    graph.add_edge("summarize",    "format")
    graph.add_conditional_edges("format", route_delivery)
    graph.add_edge("send_email",    END)
    graph.add_edge("send_whatsapp", END)

    return graph.compile()


if __name__ == "__main__":
    app = build_graph()
    result = app.invoke({})
    print("Pipeline complete — status:", result.get("status"))
