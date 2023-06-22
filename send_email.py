import smtplib
import ssl
import os

def send_email(message=""):
    host = "smtp.gmail.com"
    port = 465
    sender_username = "bryan.patrick.a.murphy@gmail.com"
    password = os.getenv("WebPortfolio_Password")

    recipient = "bryan.patrick.a.murphy@gmail.com"

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(sender_username, password)
        server.sendmail(sender_username, recipient, message)


send_email()

