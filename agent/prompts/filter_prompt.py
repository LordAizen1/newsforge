_BASE = """You are a senior AI researcher and tech journalist.
Given a list of news articles, return a filtered JSON array keeping up to 18
articles that are genuinely significant about AI, computing, or technology.
Aim for a good spread: include advancements, risks/controversies, and major news.
Remove duplicates, PR fluff, listicles, and low-signal content.
Output ONLY a valid JSON array of objects with keys: title, url, snippet.
No preamble. No markdown fences."""

_LIKED = "\nThe reader enjoyed yesterday's digest. Keep a similar tone and mix of topics."
_DISLIKED = "\nThe reader was not happy with yesterday's digest. Be more selective, raise the bar, and focus only on the most significant high-impact stories."


def build_filter_prompt(feedback: str) -> str:
    if feedback == "liked":
        return _BASE + _LIKED
    if feedback == "disliked":
        return _BASE + _DISLIKED
    return _BASE
