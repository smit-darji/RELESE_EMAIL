import ssl
import smtplib

smtp_server = "smtp.gmail.com"
port = 587  # for starttls
sender_email = "smit.softvan@gmail.com"
password = "qmkbtqileavaxwnq"

# create a secure connection with the server and starttls
context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.starttls(context=context)
    server.login(sender_email, password)
    
    # send the message
    message = "Subject: Hi there!\n\nThis is a test message."
    recipient_email = "sahilvandra.softvan@gmail.com"
    server.sendmail(sender_email, recipient_email, message)

# close the connection to the SMTP server
