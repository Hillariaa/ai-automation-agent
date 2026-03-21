import os
import requests

RESEND_API_KEY = os.getenv("RESEND_API_KEY")


def send_email(to_email: str, subject: str, message: str):

    if not RESEND_API_KEY:
        print(" Missing RESEND_API_KEY")
        return

    url = "https://api.resend.com/emails"

    headers = {
        "Authorization": f"Bearer {RESEND_API_KEY}",
        "Content-Type": "application/json",
    }

    data = {
        "from": "onboarding@resend.dev",
        "to": [to_email],
        "subject": subject,
        "html": f"<p>{message}</p>",
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        print(" Email sent:", response.json())
    except Exception as e:
        print(" Email error:", e)
