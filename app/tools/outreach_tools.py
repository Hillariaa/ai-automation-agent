PORTFOLIO_LINK = "https://ai-portfolio-rust-five.vercel.app"
CV_LINK = "https://ai-portfolio-rust-five.vercel.app/Hilary_Azimoh_AI_Engineer_CV.pdf"
CALENDLY_LINK = "https://calendly.com/hilariezee/30min"


def portfolio_response():
    return {
        "message": "You can explore Hilary's AI projects and systems here:",
        "actions": [
            {"label": "Open Portfolio", "url": PORTFOLIO_LINK},
        ],
    }


def cv_response():
    return {
        "message": "You can view Hilary's CV here:",
        "actions": [
            {"label": "Download CV", "url": CV_LINK},
        ],
    }


def calendly_response():
    return {
        "message": "Great! You can schedule a call with Hilary here:",
        "actions": [
            {"label": "Schedule Meeting", "url": CALENDLY_LINK},
        ],
    }
