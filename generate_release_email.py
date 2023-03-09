import os
import requests
from datetime import datetime, timedelta
from jinja2 import Environment, FileSystemLoader
import smtplib
import requests
import smtplib
from email.mime.text import MIMEText

# Set up the Jinja2 environment
env = Environment(loader=FileSystemLoader('.'))

# Define the GitHub API endpoint
api_url = 'https://api.github.com'

# Get the repository name and owner from the environment variables
# repo_name = os.environ.get('GITHUB_REPOSITORY')
# repo_owner = repo_name.split('/')[0]
repo_name = "smit-darji"
repo_owner = "RELESE_EMAIL"
print(repo_owner)

# Set up the authentication headers
auth_header = {
    'Authorization': f'token {os.environ.get("GITHUB_TOKEN")}',
    'Accept': 'application/vnd.github.v3+json'
}

# Query the GitHub API for the latest release
response = requests.get(
    f'{api_url}/repos/smit-darji/RELESE_EMAIL/releases/latest',
    headers=auth_header
)

if response.status_code != 200:
    raise Exception(f"Failed to retrieve releases. Error code: {response.status_code}")

latest_release = response.json()
print(latest_release)

# Render the email template using Jinja2
template = env.get_template('release_email_template.j2')
# email_body = template.render(repo_owner=repo_owner, repo_name=repo_name, latest_release=latest_release)

# Output the email body
# print(email_body)

# Send the email using SMTP
# smtp_server = os.environ.get('SMTP_SERVER')
# smtp_port = os.environ.get('SMTP_PORT')
# smtp_username = os.environ.get('SMTP_USERNAME')
# smtp_password = os.environ.get('SMTP_PASSWORD')
# sender_email = os.environ.get('SENDER_EMAIL')
# recipient_email = os.environ.get('RECIPIENT_EMAIL')

# with smtplib.SMTP(smtp_server, smtp_port) as smtp:
#     smtp.starttls()
#     smtp.login(smtp_username, smtp_password)
#     message = f'Subject: New release for {repo_name}\n\n{email_body}'
#     smtp.sendmail(sender_email, recipient_email, message)


releases = [
    {
        "name": release["name"],
        "tag_name": release["tag_name"],
        "url": release["html_url"],
        "published_at": datetime.datetime.fromisoformat(release["published_at"][:-1]),
        "body": release["body"]
    }
    for release in response.json()
    if start_date <= datetime.datetime.fromisoformat(release["published_at"][:-1]) <= end_date
]
print(releases)
# msg['Subject'] = f"New latest_release of {latest_release['tag_name']}"
# msg['From'] = 'sender@example.com'
# msg['To'] = 'recipient@example.com'