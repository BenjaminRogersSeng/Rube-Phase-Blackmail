import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(sender_email, sender_password, recipient_email, subject, body):
    # Create the message container
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Attach the email body
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Set up the SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)  # Replace with your SMTP server and port
        server.starttls()  # Upgrade the connection to a secure encrypted TLS/SSL connection
        server.login(sender_email, sender_password)
        
        # Send the email
        server.send_message(msg)
        server.quit()
        print(f"Email sent successfully to {recipient_email}")
    except Exception as e:
        print(f"Failed to send email. Error: {e}")

if __name__ == "__main__":
    # Sender's email credentials
    sender_email = "c3351499@uon.edu.au"
    sender_password = "Jabrils83!"

    # Recipient's email
    recipient_email = "rogersb.business@gmail.com"

    # Email content
    subject = "Please move this file!"
    body = "We know where you live, please move the file test.txt to the upper directory"

    # Send the email
    send_email(sender_email, sender_password, recipient_email, subject, body)
