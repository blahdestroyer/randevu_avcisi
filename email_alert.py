import smtplib
import os
from email.mime.text import MIMEText

def send_email(konu, icerik):
    gmail_user = os.getenv("EMAIL_USER")
    gmail_password = os.getenv("EMAIL_PASS")

    msg = MIMEText(icerik)
    msg["Subject"] = konu
    msg["From"] = gmail_user
    msg["To"] = gmail_user

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(gmail_user, gmail_password)
            server.sendmail(gmail_user, [gmail_user], msg.as_string())
            print("[MAIL] E-posta gönderildi.")
    except Exception as e:
        print(f"[MAIL HATA] Gönderilemedi: {e}")