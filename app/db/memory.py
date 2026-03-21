from datetime import datetime

USER_DB = {}


def get_user(user_id: str):
    return USER_DB.get(user_id)


def create_user(user_id: str, context: dict):
    USER_DB[user_id] = {
        "id": user_id,
        "source": context.get("source"),
        "persona": context.get("persona"),
        "campaign": context.get("campaign"),
        "goal": "get_job",
        "progress": [],
        "applied_jobs": [],
        "last_active": datetime.utcnow(),
        "created_at": datetime.utcnow(),
        "is_high_intent": False,
        #  TEMP TEST EMAIL
        "email": "your_email@example.com",
    }
    return USER_DB[user_id]


def update_user(user_id: str, key: str, value):
    if user_id in USER_DB:
        USER_DB[user_id][key] = value


#  NEW: detect intent
def update_intent(user_id: str):
    user = USER_DB.get(user_id)

    if not user:
        return

    if len(user["progress"]) >= 2:
        user["is_high_intent"] = True
