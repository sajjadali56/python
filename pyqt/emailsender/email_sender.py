import smtplib, ssl

with open(".env", "r") as f:
    lines = f.readlines()

port = 465
smtp_server = "smtp.gmail.com"
sender = lines[0].split("=")[1].strip()
password = lines[1].split("=")[1].strip()

print(sender, password)

def send_email(recipient, subject, body):
    context = ssl.create_default_context()

    # Format the email message with Subject, From, and To headers
    email_message = f"Subject: {subject}\nFrom: {sender}\nTo: {recipient}\n\n{body}"

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as smtp:
        smtp.login(sender, password)
        smtp.sendmail(sender, recipient, email_message)

# Example usage:
# send_email("recipient@example.com", "Test Subject", "This is the body of the email.")
