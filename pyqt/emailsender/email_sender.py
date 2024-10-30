import smtplib, ssl

with open(".env", "r") as f:
    lines = f.readlines()

port = 465
smtp_server = "smtp.gmail.com"
sender = lines[0].split("=")[1].strip()
password = lines[1].split("=")[1].strip()

context = ssl.create_default_context()

def send_email(recipient, subject, body):
    email_message = f"Subject: {subject}\nFrom: {sender}\nTo: {recipient}\n\n{body}"

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as smtp:
        smtp.login(sender, password)
        smtp.sendmail(sender, recipient, email_message)
