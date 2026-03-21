# app/outreach/linkedin_helper.py

from app.outreach.agent import generate_initial_message, generate_link


def generate_linkedin_messages(leads):
    """
    Generates copy-paste LinkedIn messages
    """

    results = []

    for lead in leads:
        link = generate_link(lead["role"])
        message = generate_initial_message(lead, link)

        results.append({"name": lead["name"], "message": message.strip()})

    return results


if __name__ == "__main__":
    leads = [
        {"name": "Sarah", "role": "AI Hiring Manager"},
        {"name": "David", "role": "Technical Recruiter"},
    ]

    messages = generate_linkedin_messages(leads)

    for m in messages:
        print("------")
        print(m["name"])
        print(m["message"])
