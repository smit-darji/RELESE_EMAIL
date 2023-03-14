from email.mime.text import MIMEText
import ssl
import smtplib
from datetime import datetime
from datetime import timedelta
from github import Github

smtp_server = "smtp.gmail.com"
port = 587  # for starttls
sender_email = "smit.softvan@gmail.com"
password = "qmkbtqileavaxwnq"


# create a GitHub instance using a personal access token
g = Github("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")

# get the Python repository by name
repo = g.get_repo("smit-darji/RELESE_EMAIL")

today = datetime.utcnow().date()
last_week = today - timedelta(days=7)

# get all releases for the last 7 days
releases = repo.get_releases()
recent_releases = [release for release in releases if release.published_at.date() > last_week]

# loop through recent releases and print their version and body details

email_body = ""
for release in recent_releases:
    email_body += f"Release: {release.title}\n"
    email_body += f"Version: {release.tag_name}\n"
    email_body += f"Body:\n{release.body}\n\n"

# set up the email message
print(email_body)
context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.starttls(context=context)
    server.login(sender_email, password)
    
    # send the message
    message = ("Subject: Hi there!\n\n{0}".format(email_body))
    recipient_email = "sahilvandra.softvan@gmail.com"
    server.sendmail(sender_email, recipient_email, message)