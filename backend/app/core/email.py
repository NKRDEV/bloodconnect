import os
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from app.config.settings import settings


def str_to_bool(value: str) -> bool:
    return value.lower() == "true"


conf = ConnectionConfig(
    MAIL_USERNAME=settings.SMTP_USER,
    MAIL_PASSWORD=settings.SMTP_PASSWORD,
    MAIL_FROM=settings.EMAIL_FROM,
    MAIL_PORT=settings.SMTP_PORT,
    MAIL_SERVER=settings.SMTP_HOST,
    MAIL_FROM_NAME="BloodConnect",


    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True,
)

fast_mail = FastMail(conf)


async def send_reset_email(email: str, token: str):
    reset_link = f"{settings.FRONTEND_URL}/reset-password?token={token}"

    message = MessageSchema(
        subject="Reset your BloodConnect password",
        recipients=[email],
        body=f"""
        Hello,

        Click the link below to reset your password:

        {reset_link}

        This link expires in 15 minutes.

        — BloodConnect Team
        """,
        subtype="plain",
    )

    await fast_mail.send_message(message)
