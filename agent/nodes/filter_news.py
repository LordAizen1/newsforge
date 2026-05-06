import json
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
from agent.prompts.filter_prompt import SYSTEM

llm = ChatOpenAI(model="gpt-4o-mini", max_tokens=2048)


def run(state: dict) -> dict:
    articles = state["raw_articles"]
    payload = json.dumps([
        {"title": a["title"], "url": a["url"], "snippet": a.get("content", "")[:400]}
        for a in articles
    ])
    resp = llm.invoke([SystemMessage(content=SYSTEM), HumanMessage(content=payload)])
    filtered = json.loads(resp.content)
    print(f"[filter] kept {len(filtered)} / {len(articles)} articles")
    return {"filtered": filtered}
