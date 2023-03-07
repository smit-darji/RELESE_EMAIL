import os
import requests
from datetime import datetime, timedelta
from jinja2 import Environment, FileSystemLoader
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Set up the Jinja2 environment
env = Environment(loader=FileSystemLoader('.'))

# Define the GitHub API endpoint
api_url = 'https://api.github.com'

# Get the repository name and owner from the environment variables
# repo_name = os.environ.get('GITHUB_REPOSITORY')
# repo_owner = repo_name.split('/')[0]

# Set up the authentication headers
auth_header = {
    'Authorization': f'token {os.environ.get("GITHUB_TOKEN")}',
    'Accept': 'application/vnd.github.v3+json'
}

# Query the GitHub API for the last release
response = requests.get(
    f'{api_url}/repos/smit-darji/RELESE_EMAIL/releases/latest',
    headers=auth_header
)

# Get the release details
release = response.json()
print(release)
release_name = release['name']
release_date = datetime.fromisoformat(release['published_at'][:-1]).strftime('%Y-%m-%d %H:%M:%S')
release_url = release['html_url']

# Render the email template using Jinja2
template = env.get_template('release_email_template.j2')
email_body = template.render(repo_owner="smit-darji", repo_name="RELESE_EMAIL", release_name=release_name, release_date=release_date, release_url=release_url)

# Set up the email message
msg = MIMEMultipart()
msg['Subject'] = 'New Release!'
msg['From'] = 'smit.softvan@gmail.com'
msg['To'] = 'sahil.vandra@gmail.com'

# Attach the email body to the message
body = MIMEText(email_body, 'html')
msg.attach(body)

# Send the email using SMTP
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.starttls()
    smtp.login("sender@example.com", "password")
    smtp.send_message(msg)