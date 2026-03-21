from app.outreach.leads import get_leads
from app.outreach.sender import send_email

BASE_URL = "https://ai-career-agent-ui.vercel.app"


def generate_link(persona):
    return f"{BASE_URL}?source=outreach&persona={persona}"


def generate_initial_message(name, role, link):

    return f"""
Hey {name},

I built an AI-powered career assistant that walks through my projects, systems, and experience as an AI Engineer.

Since you're a {role}, I thought this might be relevant.

You can interact with it here:
{link}
"""


def run_outreach():

    leads = get_leads()

    for lead in leads:
        link = generate_link(lead["role"])

        message = generate_initial_message(lead["name"], lead["role"], link)

        send_email(to_email=lead["email"], subject="Quick intro", message=message)
