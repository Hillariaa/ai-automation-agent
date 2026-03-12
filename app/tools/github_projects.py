import os
import requests
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

GITHUB_USERNAME = "Hillariaa"


def fetch_projects():

    url = f"https://github.com/{GITHUB_USERNAME}?tab=repositories"

    try:
        response = requests.get(url)

        if response.status_code != 200:
            return []

        html = response.text

    except Exception:
        return []

    projects = []

    # simple repo name extraction
    parts = html.split('itemprop="name codeRepository"')

    for part in parts[1:]:
        repo = part.split(">")[1].split("<")[0].strip()

        projects.append(
            {
                "name": repo,
                "description": "AI engineering project",
                "url": f"https://github.com/{GITHUB_USERNAME}/{repo}",
            }
        )

    return projects


def get_repo_names():

    projects = fetch_projects()

    return [p["name"] for p in projects]


def fetch_readme(repo_name):

    url = f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{repo_name}/main/README.md"

    try:
        response = requests.get(url)

        if response.status_code != 200:
            return None

        return response.text

    except Exception:
        return None


def explain_project_architecture(repo_name):

    readme = fetch_readme(repo_name)

    if not readme:
        return f"{repo_name} is one of Hilary's AI engineering projects."

    prompt = f"""
Hilary is an Applied AI Engineer.

Below is the README of one of her GitHub projects.

README:

{readme}

Explain this AI system clearly for a recruiter.

Include:

• what problem the system solves
• the architecture of the system
• key technologies used
• how the AI works

Keep the explanation concise and professional.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
    )

    return (response.choices[0].message.content or "").strip()


def explain_projects():

    ai_projects = [
        "ai-research-agent",
        "ai-interview-intelligence",
        "ai-knowledge-copilot",
        "ai-automation-agent",
        "ai-career-agent-ui",
    ]

    explanations = []

    for repo in ai_projects:
        readme = fetch_readme(repo)

        if not readme:
            continue

        prompt = f"""
Hilary is an Applied AI Engineer.

Below is the README of one of her AI systems.

Repository: {repo}

README:

{readme}

Explain the system clearly for a recruiter.

Rules:
- clean plain text
- no markdown
- no asterisks
- short paragraphs

Include:
• what the system does
• the architecture
• key technologies used
• how the AI works
"""

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
        )

        text = (response.choices[0].message.content or "").strip()

        explanations.append(text)

    if not explanations:
        return "Hilary has built several applied AI systems across her GitHub repositories."

    return "\n\n".join(explanations)
