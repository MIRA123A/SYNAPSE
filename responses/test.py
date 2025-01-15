import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email settings
smtp_server = 'in-v3.mailjet.com'
smtp_port = 587
sender_email = "9ebdc63aba0d5a49d1c999cefbe62a05"  # Remplacez par votre clé API Mailjet
sender_password = "673e979fa618cf465ada087a98718afb" # Remplacez par votre clé secrète API Mailjet
receiver_email = "ousamamechergui@gmail.com"
sender_email_real = "synapsemohamed@gmail.com"  # Remplacez par votre adresse email vérifiée sur Mailjet


# Email content
message = MIMEMultipart("alternative")
message["Subject"] = "Test Email from test.py"
message["From"] = sender_email_real
message["To"] = receiver_email
message["Reply-To"] = sender_email_real

html = """
<html>
  <body>
    <p>Bonjour,</p>
    <p>This is a test email sent using the provided Brevo SMTP details.</p>
  </body>
</html>
"""
part = MIMEText(html, "html")
message.attach(part)

# Create secure connection
context = ssl.create_default_context()
try:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls(context=context)  # Secure the connection
        server.login(sender_email, sender_password)
        server.sendmail(sender_email_real, receiver_email, message.as_string())
        print("Email Sent Successfully!")
except smtplib.SMTPAuthenticationError as e:
        print(f"SMTP Authentication error: {e}")
except Exception as e:
    print(f"Error sending email: {e}")