import smtplib
from email.mime.text import MIMEText

def send_honeypot_reply(to_email: str, fake_content: str):
    msg = MIMEText(fake_content)
    msg['Subject'] = "Re: Your Message"
    msg['From'] = "honeypot@yourdomain.com"
    msg['To'] = to_email
    with smtplib.SMTP('localhost') as server:  # Stub; use secure SMTP
        server.send_message(msg)