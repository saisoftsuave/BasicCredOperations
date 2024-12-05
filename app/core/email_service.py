# Configuration
import smtplib
from email.message import EmailMessage

from fastapi import BackgroundTasks
from itsdangerous import URLSafeTimedSerializer
from pydantic import EmailStr

EMAIL_ADDRESS = "saibabu.ss806@gmail.com"  # Replace with your email
EMAIL_PASSWORD = "zhjs ghhh sjkj tisu"  # Replace with your email password
BASE_URL = "http://127.0.0.1:8000/api/v1/auth"  # Replace with your app's base URL


def send_email(to_email: str, subject: str, body: str):
    try:
        msg = EmailMessage()
        msg["Subject"] = subject
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = to_email
        msg.set_content(body)

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
    except Exception as e:
        print(f"Failed to send email: {e}")


def request_verification(email: str, token: str):

    # Generate verification link
    verification_link = f"{BASE_URL}/verify-email/{token}"

    # Send email in the background
    subject = "Email Verification"
    body = f"Please click the link to verify your email: {verification_link}"
    send_email(email, subject, body)
