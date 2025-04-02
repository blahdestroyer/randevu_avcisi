import smtplib
from email.mime.text import MIMEText

def send_email(konu, icerik):
    gmail_user = "marvin.ordinarus@gmail.com"
    gmail_password = "fway lxxi vuhj syal"  # Uygulama şifresi

    msg = MIMEText(icerik)
    msg["Subject"] = konu
    msg["From"] = gmail_user
    msg["To"] = gmail_user

    try:
        with smtpllib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(gmail_user, gmail_password)
            server.sendmail(gmail_user, [gmail_user], msg.as_string())
            print("[MAIL] E-posta gönderildi.")
    except Exception as e:
        print(f"[MAIL HATA] Gönderilemedi: {e}")