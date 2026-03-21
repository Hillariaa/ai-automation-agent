# app/outreach/leads.py


def is_valid_lead(role: str) -> bool:
    """
    Filters ONLY high-signal roles.
    """

    role = role.lower()

    valid_keywords = [
        "hiring manager",
        "technical recruiter",
        "talent partner",
        "head of ai",
        "engineering manager",
    ]

    learning_roles = [
        "ai engineer",  # for networking / learning
    ]

    # reject low-signal roles
    excluded_keywords = [
        "junior",
        "student",
        "intern",
    ]

    if any(x in role for x in excluded_keywords):
        return False

    if any(x in role for x in valid_keywords + learning_roles):
        return True

    return False


def get_leads():
    """
    Replace later with LinkedIn scraping / CSV / Apollo.
    """

    raw_leads = [
        {"name": "Sarah", "email": "sarah@company.com", "role": "AI Hiring Manager"},
        {"name": "David", "email": "david@company.com", "role": "Technical Recruiter"},
        {"name": "Emily", "email": "emily@company.com", "role": "HR Manager"},
        {
            "name": "Michael",
            "email": "michael@company.com",
            "role": "Engineering Manager",
        },
        {"name": "Lena", "email": "lena@company.com", "role": "AI Engineer"},
        {"name": "Tom", "email": "tom@company.com", "role": "Junior Developer"},
    ]

    filtered = [lead for lead in raw_leads if is_valid_lead(lead["role"])]

    return filtered
