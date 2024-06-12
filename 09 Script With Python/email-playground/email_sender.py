import smtplib
from email.message import EmailMessage
from pathlib import path
from string import Template

html = Template(path("index.html").read_text())
email = EmailMessage()
email["from"] = ("Nama",)
email["to"] = ("traget@gmail.com",)
email["subject"] = "Halloooo"

email.set_content(html.substitute({"content": "Hello my friend how are you?"}), "html")

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("email", "password")
    smtp.send_message(email)
    print("Email sent success!")
