import os
from tavily import TavilyClient

client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

QUERIES = [
    "AI model release breakthrough 2026",
    "artificial intelligence safety regulation news",
    "tech startup funding acquisition today",
    "LLM computing hardware announcement",
    "AI layoffs risks controversy this week",
]


def run(state: dict) -> dict:
    articles = []
    seen_urls = set()
    for query in QUERIES:
        results = client.search(
            query,
            topic="news",
            days=1,
            search_depth="basic",
            max_results=8,
        )
        for article in results.get("results", []):
            if article["url"] not in seen_urls:
                seen_urls.add(article["url"])
                articles.append(article)
    print(f"[search] fetched {len(articles)} unique articles")
    return {"raw_articles": articles}
