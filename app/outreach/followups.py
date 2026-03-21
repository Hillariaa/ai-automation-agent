from app.db.memory import USER_DB


def run_followups():
    """
    Only follow up HIGH INTENT users
    """

    for user in USER_DB.values():
        if user["is_high_intent"] and user["source"] == "outreach":
            print(f"""
FOLLOW-UP TRIGGERED:

User: {user["id"]}
Persona: {user["persona"]}

Message:
Hey — saw you checked out the assistant.

Happy to walk through anything or answer questions.
""")
