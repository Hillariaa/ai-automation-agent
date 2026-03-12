import os
import requests
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

GITHUB_USERNAME = "Hillariaa"


def fetch_projects():

    url = f"https://api.github.com/users/{GITHUB_USERNAME}/repos"

    try:
        response = requests.get(url)
        response.raise_for_status()
        repos = response.json()
    except Exception:
        return []

    projects = []

    for repo in repos:
        projects.append(
            {
                "name": repo.get("name"),
                "description": repo.get("description"),
                "url": repo.get("html_url"),
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
        return "Sorry, I couldn't retrieve the project documentation."

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

Keep the explanation clear, concise, and professional.
Focus on engineering and AI aspects.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
    )

    content = response.choices[0].message.content or ""

    return content.strip()


def explain_projects():

    projects = fetch_projects()

    if not projects:
        return "Hilary has built several applied AI systems available on her GitHub."

    project_text = ""

    for p in projects:
        name = p["name"]
        description = p["description"] or "AI engineering project"

        project_text += f"{name}: {description}\n"

    prompt = f"""
Hilary is an Applied AI Engineer.

These are her GitHub repositories:

{project_text}

Explain the most important AI systems she built.

Focus on:

• what each system does
• the AI techniques used
• the engineering architecture
• the technologies used

Keep the explanation clear for recruiters.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
    )

    content = response.choices[0].message.content or ""

    return content.strip()
