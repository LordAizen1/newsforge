import json
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
from agent.prompts.summarize_prompt import SYSTEM

llm = ChatOpenAI(model="gpt-4o-mini", max_tokens=4096)


def run(state: dict) -> dict:
    articles = state["categorized"]
    resp = llm.invoke([SystemMessage(content=SYSTEM), HumanMessage(content=json.dumps(articles))])
    sections = json.loads(resp.content)
    print(f"[summarize] wrote {len(sections)} summaries")
    return {"digest_sections": sections}
