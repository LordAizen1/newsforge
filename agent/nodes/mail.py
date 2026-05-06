import os
from datetime import date
import sendgrid
from sendgrid.helpers.mail import Mail


def run(state: dict) -> dict:
    sg = sendgrid.SendGridAPIClient(api_key=os.getenv("SENDGRID_API_KEY"))
    today = date.today().strftime("%A, %B %d, %Y")
    message = Mail(
        from_email=os.getenv("SENDER_EMAIL"),
        to_emails=os.getenv("RECIPIENT_EMAIL"),
        subject=f"Your Daily AI + Tech Digest — {today}",
        html_content=state["email_html"],
    )
    response = sg.send(message)
    print(f"[mail] sent — HTTP {response.status_code}")
    return {"status": "success"}
