# AI Career Automation Agent

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green)
![LangGraph](https://img.shields.io/badge/LangGraph-Agent%20Framework-purple)
![OpenAI](https://img.shields.io/badge/OpenAI-LLM-black)
![Next.js](https://img.shields.io/badge/Next.js-Frontend-lightgrey)
![AI Agents](https://img.shields.io/badge/AI-Agent%20System-orange)
![Deployment](https://img.shields.io/badge/Deployment-Render%20%7C%20Vercel-blue)

AI-powered automation agent that interacts with recruiters by answering questions about my work, sharing my portfolio and CV, and helping schedule calls.

---

## Overview

The AI Career Agent acts as a conversational interface for recruiters.

Instead of manually answering questions or sending information repeatedly, the agent can:

• Explain my AI systems  
• Share my portfolio and GitHub  
• Provide my CV  
• Help schedule calls via Calendly  

The system demonstrates practical AI agent design using LangGraph and LLM routing.

---

## Tech Stack

- Python
- FastAPI
- LangGraph
- OpenAI API
- Next.js
- TypeScript
- AI Agents
- Automation Workflows

  
## System Architecture

The AI Career Automation Agent is composed of three main components.

```text
Recruiter
   │
   ▼
Next.js UI (AI Career Agent Interface)
   │
   ▼
FastAPI Backend
   │
   ▼
LangGraph Agent Workflow
   │
   ├─ Knowledge Node → Explains AI systems
   ├─ Portfolio Node → Shares portfolio
   ├─ CV Node → Sends CV
   └─ Schedule Node → Links to Calendly
   │
   ▼
OpenAI GPT Model
```

In summary:

Frontend  
Next.js conversational UI

Backend  
FastAPI API hosting the AI agent

Agent Framework  
LangGraph state machine managing conversation flow

AI Model  
OpenAI GPT models

Deployment  
Render (backend)  
Vercel (frontend)

---

## Example Interaction

Recruiter:  
"Tell me about Hilary's work."

Agent:

- AI Research Agent – autonomous research system
- AI Interview Intelligence – speech + LLM analysis system
- AI Knowledge Copilot – RAG knowledge assistant
- AI Career Automation Agent – recruiter interaction system

Recruiter can then schedule a call.

---

## Live Demo

https://ai-career-agent-ui.vercel.app

---

## Portfolio

https://ai-portfolio-rust-five.vercel.app

---

## Author

Hilary Azimoh  
Applied AI Engineer
