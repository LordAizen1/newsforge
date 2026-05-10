import json
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
from agent.prompts.filter_prompt import build_filter_prompt

llm = ChatOpenAI(model="gpt-4o-mini", max_tokens=2048)


def run(state: dict) -> dict:
    articles = state["raw_articles"]
    feedback = state.get("feedback", "none")
    payload = json.dumps([
        {"title": a["title"], "url": a["url"], "snippet": a.get("content", "")[:400]}
        for a in articles
    ])
    prompt = build_filter_prompt(feedback)
    resp = llm.invoke([SystemMessage(content=prompt), HumanMessage(content=payload)])
    filtered = json.loads(resp.content)
    print(f"[filter] kept {len(filtered)} / {len(articles)} articles")
    return {"filtered": filtered}
