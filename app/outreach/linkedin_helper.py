from app.outreach.agent import generate_link, generate_initial_message


def generate_linkedin_messages(leads):
    """
    Generate outreach messages for LinkedIn manually
    """

    results = []

    for lead in leads:
        link = generate_link(lead["role"])

        message = generate_initial_message(lead["name"], lead["role"], link)

        results.append({"name": lead["name"], "role": lead["role"], "message": message})

    return results


# 🔥 TEST BLOCK
if __name__ == "__main__":
    leads = [
        {"name": "Sarah", "role": "AI Hiring Manager"},
        {"name": "David", "role": "Technical Recruiter"},
    ]

    results = generate_linkedin_messages(leads)

    for r in results:
        print("------")
        print(f"To: {r['name']} ({r['role']})\n")
        print(r["message"])
