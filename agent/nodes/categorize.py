import json
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
from agent.prompts.categorize_prompt import SYSTEM

llm = ChatOpenAI(model="gpt-4o-mini", max_tokens=2048)


def run(state: dict) -> dict:
    articles = state["filtered"]
    resp = llm.invoke([SystemMessage(content=SYSTEM), HumanMessage(content=json.dumps(articles))])
    categorized = json.loads(resp.content)
    print(f"[categorize] categorized {len(categorized)} articles")
    return {"categorized": categorized}
