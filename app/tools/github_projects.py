import requests
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

GITHUB_USERNAME = "Hillariaa"


def explain_project_architecture(repo_name):

    readme = fetch_readme(repo_name)

    if not readme:
        return "Sorry, I couldn't retrieve the project documentation."

    prompt = f"""
Hilary built this AI system.

Project README:

{readme}

Explain the architecture of this project clearly for a recruiter.
Focus on:
- the AI system
- the tools used
- the architecture
- what problem it solves
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
    )

    return response.choices[0].message.content


def fetch_projects():

    url = f"https://api.github.com/users/{GITHUB_USERNAME}/repos"

    try:
        response = requests.get(url)
        response.raise_for_status()
        repos = response.json()
    except Exception:
        return []

    if not repos:
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


def fetch_readme(repo_name):

    url = f"https://raw.githubusercontent.com/Hillariaa/{repo_name}/main/README.md"

    response = requests.get(url)

    if response.status_code != 200:
        return None

    return response.text


def get_repo_names():

    projects = fetch_projects()

    return [p["name"] for p in projects]


def explain_projects():

    projects = fetch_projects()

    if not projects:
        return "Hilary has built several AI systems available on her GitHub."

    project_text = ""

    for p in projects:
        project_text += f"{p['name']}: {p['description']}\n"

    prompt = f"""
Hilary is an applied AI engineer.

These are her GitHub projects:

{project_text}

Explain the most important AI systems she built in a clear way for recruiters.
Focus on AI systems and automation tools.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
    )

    content = response.choices[0].message.content or ""

    return content.strip()
