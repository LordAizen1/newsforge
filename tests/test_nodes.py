from agent.nodes import format_digest


MOCK_SECTIONS = [
    {"title": "GPT-6 released", "url": "https://example.com/1", "category": "advancements", "summary": "OpenAI released GPT-6. It sets new benchmarks across coding and reasoning."},
    {"title": "EU fines AI company", "url": "https://example.com/2", "category": "risks", "summary": "EU issued a $400M fine. This is the first major enforcement under the AI Act."},
    {"title": "Startup raises $200M", "url": "https://example.com/3", "category": "news", "summary": "AI infra startup closed a $200M Series B. The round was led by Andreessen Horowitz."},
]


def test_format_produces_email_html():
    state = {"digest_sections": MOCK_SECTIONS}
    result = format_digest.run(state)
    assert "<html" in result["email_html"]
    assert "GPT-6 released" in result["email_html"]


def test_format_produces_whatsapp_text():
    state = {"digest_sections": MOCK_SECTIONS}
    result = format_digest.run(state)
    assert "*ADVANCEMENTS*" in result["whatsapp_text"]
    assert "*RISKS & BAD NEWS*" in result["whatsapp_text"]
    assert "GPT-6 released" in result["whatsapp_text"]


def test_format_groups_correctly():
    state = {"digest_sections": MOCK_SECTIONS}
    result = format_digest.run(state)
    html = result["email_html"]
    # advancements section appears before risks
    assert html.index("Advancements") < html.index("Risks")
