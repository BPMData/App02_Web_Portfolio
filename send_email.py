import smtplib
import ssl
import os
import streamlit as st

def send_email(message=""):
    host = "smtp.gmail.com"
    port = 465
    sender_username = "bryan.patrick.a.murphy@gmail.com"
    # password = os.getenv("WebPortfolio_Password")
    password = st.secrets["EMAIL_TOKEN"]

    recipient = "bryan.patrick.a.murphy@gmail.com"

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(sender_username, password)
        server.sendmail(sender_username, recipient, message)

content = """
<html>
<head>
<style>
.bold {
    font-weight: bold;
}

.underline {
    text-decoration: underline;
}

.large {
    font-size: larger;
}
</style>
</head>
<body>
<span class="bold">Hello.</span><br><br>
<span class="large">My name is David.</span><br><br>
<span class="underline">Bye!</span>
</body>
</html>"""

send_email(content)

