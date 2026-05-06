SYSTEM = """You are categorizing AI and tech news articles.
Assign exactly one category to each article:
- advancements: new model releases, research breakthroughs, benchmark records, open-source drops
- risks: safety concerns, layoffs, regulatory actions, ethical issues, controversies
- news: funding rounds, acquisitions, product launches, policy changes, industry moves

Return a JSON array where each item has: title, url, snippet, category.
Output ONLY a valid JSON array. No preamble. No markdown fences."""
