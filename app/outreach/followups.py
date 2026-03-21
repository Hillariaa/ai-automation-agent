from app.db.memory import USER_DB
from app.outreach.sender import send_email


def run_followups():
    """
    Send follow-ups ONLY to high-intent outreach users
    """

    for user in USER_DB.values():
        if user.get("is_high_intent") and user.get("source") == "outreach":
            email = user.get("email")

            if not email:
                print(f"⚠️ No email for user {user['id']}")
                continue

            message = (
                "Hey — saw you interacted with my AI assistant.\n\n"
                "Happy to walk you through my systems or answer any questions.\n\n"
                "Best,\nHilary"
            )

            send_email(to_email=email, subject="Quick follow-up", message=message)
