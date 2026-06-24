import smtplib
import logging
import os

from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders
from dotenv import load_dotenv

load_dotenv()

SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")

def send_email(recipient,html_content,attachment_path):
    try:
        msg = MIMEMultipart()
        msg["From"] = SENDER_EMAIL
        msg["To"] = recipient
        msg["Subject"] = "Sales Report"
        msg.attach(MIMEText(html_content,"html"))
        with open(attachment_path,"rb") as attachment:
            part = MIMEBase( "application","octet-stream")
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header("Content-Disposition",f"attachment; filename={attachment_path}")
            msg.attach(part)

        server = smtplib.SMTP_SSL( "smtp.gmail.com", 465)
        server.login(SENDER_EMAIL,SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL,recipient,msg.as_string())
        server.quit()
        logging.info(f"Email sent to {recipient}" )

    except Exception as e:
        logging.error( f"Email failed for {recipient}: {e}")