# app/outreach/sender.py


def send_email(email: str, message: str):
    """
    Mock email sender (for now).
    Later replace with:
    - SendGrid
    - Resend
    - Gmail API
    """

    print("------ EMAIL SENT ------")
    print(f"To: {email}")
    print(message)
    print("------------------------")
