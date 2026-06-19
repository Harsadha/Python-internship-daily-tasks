# DAILY TASK- WEEK 3- DAY 2
'''
✓ Send plain text email via Gmail SMTP
✓ Send an HTML styled report email
✓ Attach report.csv (from Day 6) as file attachment
✓ Store SMTP credentials in .env using python dotenv
✓ Log sent/failed status per recipient'''

from dotenv import load_dotenv
import os
import smtplib
import logging

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

class EmailAutomationError(Exception):
    """when email automation fails"""
    pass

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)
logger = logging.getLogger(__name__)

logger.info("Loading environment variables...")

load_dotenv()

EMAIL = os.getenv("FROM_EMAIL")
PASSWORD = os.getenv("PASSWORD")

if not EMAIL or not PASSWORD:
    raise EmailAutomationError("FROM_EMAIL or PASSWORD not found in .env")

logger.info("Environment variables loaded successfully.")

receivers = ["harsadha2310312@ssn.edu.in","h.ranjeeth.kumar@accenture.com"]

html_body = """
<html>
<body>
    <h2 style="color:pink;">
        Daily Internship Report
    </h2>

    <p>Hello,</p>

    <p>Good Evening,<br>I have finished this week's report. Please find the attachment below.</p>

    <p>Regards,<br>Harsadha</p>
</body>
</html>
"""

try:
    logger.info("Connecting to Gmail SMTP Server...")
    server = smtplib.SMTP_SSL("smtp.gmail.com",465)
    logger.info("SMTP connection established.")
    logger.info("Authenticating Gmail account...")
    server.login(EMAIL,PASSWORD)
    logger.info("Authentication successful.")

except Exception as e:
    logger.error(f"SMTP connection/login failed: {e}")
    raise EmailAutomationError("Failed to connect/login to Gmail SMTP")

for receiver in receivers:
    logger.info( f"Preparing email for {receiver}")
    try:
        message = MIMEMultipart()
        message["From"] = EMAIL
        message["To"] = receiver
        message["Subject"] = "Weekly Internship Report"
        message.attach(MIMEText(html_body,"html"))
        logger.info(f"HTML content attached for {receiver}")

        csv_path = "C:/Users/h.ranjeeth.kumar/OneDrive - Accenture/Documents/Project/Code/19-6-2026-task/report.csv"
        if not os.path.exists(csv_path):
            raise FileNotFoundError(f"{csv_path} not found.")

        with open(csv_path,"rb") as file:
            attachment = MIMEBase("application","octet-stream")
            attachment.set_payload(file.read())

        encoders.encode_base64(attachment)

        attachment.add_header("Content-Disposition",f"attachment; filename={os.path.basename(csv_path)}")

        message.attach(attachment)

        logger.info(f"CSV attachment added for {receiver}")

        logger.info(
            f"Sending email to {receiver}"
        )

        server.sendmail(EMAIL, receiver, message.as_string())

        logger.info(f"SUCCESS -> Email sent to {receiver}")

    except EmailAutomationError as custom_error:
        logger.error( f"CUSTOM ERROR for {receiver}: {custom_error}")

    except Exception as e:
        logger.error(f"FAILED -> {receiver}: {e}")

try:
    server.quit()
    logger.info( "SMTP connection closed successfully.")

except Exception as e:
    logger.error(f"Error closing SMTP connection: {e}")