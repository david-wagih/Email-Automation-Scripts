import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import ssl


def send_email(sender_email, receiver_email, subject, body):
    """
    Sends an email using the provided sender email address and credentials.

    Args:
        sender_email (str): Email address of the sender.
        receiver_email (str): Email address of the recipient.
        subject (str): Subject of the email.
        body (str): Content of the email body.
    """

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    message.attach(MIMEText(body, "plain"))  # Set content type as plain text

    # Replace with your actual SMTP server details and password (secure your password)
    smtp_server = "smtp.your-email-provider.com"
    smtp_port = 587  # Adjust port if needed (e.g., 465 for SSL)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
        server.login(sender_email, "your_password")
        server.sendmail(sender_email, receiver_email, message.as_string())
        print(f"Email sent to: {receiver_email}")


def send_emails_in_batches(sender_email, batch_files):
    """
    Sends emails in batches using the provided sender email and batch files.

    Args:
        sender_email (str): Email address of the sender.
        batch_files (list): List of file paths for the batch email files.
    """

    for batch_file in batch_files:
        with open(batch_file, "r") as infile:
            for line in infile:
                receiver_email = line.strip()
                subject = "Your Subject Here"  # Replace with your desired subject
                body = "Your Email Body Here"  # Replace with your email message
                send_email(sender_email, receiver_email, subject, body)


# Example usage (replace placeholders)
sender_email = "info@slash-eg.com"  # Update with your actual email address

# Get list of batch files from the previous script's output (modify as needed)
batch_files = [
    "batch_1.txt",
    "batch_2.txt",
    ...,
]  # Replace with your actual batch files

send_emails_in_batches(sender_email, batch_files)
