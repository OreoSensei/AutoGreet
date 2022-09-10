import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
import os

sender_email = os.getenv("SENDER_EMAIL")
password = os.getenv("SENDER_PASSWORD")

def sendMail(receiver_email, bodyMessage):
    message = MIMEMultipart("alternative")
    message["Subject"] = "RE: Your automatic birthday wisher"
    message["From"] = sender_email
    message["To"] = receiver_email

    # # Turn these into plain/html MIMEText objects
    part1 = MIMEText(bodyMessage, "plain")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            time.sleep(10)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )
            time.sleep(5)

        return "Mail sent"
    except Exception as e:
        print(e)
        return "Mail could not sent Exception is : {}".format(e)