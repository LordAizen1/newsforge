import os
from datetime import date
from jinja2 import Environment, FileSystemLoader

_TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "templates")
_env = Environment(loader=FileSystemLoader(os.path.abspath(_TEMPLATES_DIR)))

CATEGORY_EMOJI = {"advancements": "🚀", "risks": "⚠️", "news": "📰"}
CATEGORY_LABEL = {"advancements": "ADVANCEMENTS", "risks": "RISKS & BAD NEWS", "news": "MAJOR NEWS"}


def _group(sections: list) -> dict:
    grouped = {"advancements": [], "risks": [], "news": []}
    for s in sections:
        cat = s.get("category", "news")
        grouped.setdefault(cat, []).append(s)
    return grouped


def _whatsapp_text(sections: list, today: str) -> str:
    grouped = _group(sections)
    lines = [f"*Your Daily AI Digest — {today}*\n"]
    for cat in ("advancements", "risks", "news"):
        items = grouped.get(cat, [])
        if not items:
            continue
        lines.append(f"{CATEGORY_EMOJI[cat]} *{CATEGORY_LABEL[cat]}*")
        for item in items:
            lines.append(f"• {item['title']}")
            lines.append(f"  _{item.get('summary', '')}_ \n")
    return "\n".join(lines)


def run(state: dict) -> dict:
    sections = state["digest_sections"]
    today = date.today().strftime("%A, %B %d, %Y")
    grouped = _group(sections)

    email_html = _env.get_template("email.html").render(
        today=today,
        advancements=grouped["advancements"],
        risks=grouped["risks"],
        news=grouped["news"],
    )
    whatsapp_text = _whatsapp_text(sections, today)
    print("[format] rendered email HTML and WhatsApp text")
    return {"email_html": email_html, "whatsapp_text": whatsapp_text}
