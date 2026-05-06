import os
from twilio.rest import Client

CHUNK_LIMIT = 1500


def _chunk_by_lines(text: str, limit: int) -> list:
    lines = text.split("\n")
    chunks = []
    current_lines = []
    current_len = 0

    for line in lines:
        line_len = len(line) + 1  # +1 for the newline
        if current_lines and current_len + line_len > limit:
            chunks.append("\n".join(current_lines))
            current_lines = [line]
            current_len = line_len
        else:
            current_lines.append(line)
            current_len += line_len

    if current_lines:
        chunks.append("\n".join(current_lines))

    return chunks


def run(state: dict) -> dict:
    client = Client(os.getenv("TWILIO_ACCOUNT_SID"), os.getenv("TWILIO_AUTH_TOKEN"))
    chunks = _chunk_by_lines(state["whatsapp_text"], CHUNK_LIMIT)
    from_number = f"whatsapp:{os.getenv('TWILIO_WHATSAPP_FROM')}"
    to_number = f"whatsapp:{os.getenv('WHATSAPP_RECIPIENT')}"
    for i, chunk in enumerate(chunks, 1):
        msg = client.messages.create(from_=from_number, to=to_number, body=chunk)
        print(f"[whatsapp] chunk {i}/{len(chunks)} sent — sid {msg.sid}")
    return {"status": "success"}
