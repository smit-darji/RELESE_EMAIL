import os
import requests
from datetime import datetime, timedelta
from jinja2 import Environment, FileSystemLoader
import smtplib
import requests

# Set up the Jinja2 environment
env = Environment(loader=FileSystemLoader('.'))

# Define the GitHub API endpoint
api_url = 'https://api.github.com'

# Get the repository name and owner from the environment variables
repo_name = os.environ.get('GITHUB_REPOSITORY')
repo_owner = repo_name.split('/')[0]

# Set up the authentication headers
auth_header = {
    'Authorization': f'token {os.environ.get("GITHUB_TOKEN")}',
    'Accept': 'application/vnd.github.v3+json'
}

# Query the GitHub API for the latest release
response = requests.get(
    f'{api_url}/repos/{repo_owner}/{repo_name}/releases/latest',
    headers=auth_header
)
latest_release = response.json()

# Render the email template using Jinja2
template = env.get_template('release_email_template.j2')
email_body = template.render(repo_owner=repo_owner, repo_name=repo_name, latest_release=latest_release)

# Output the email body
print(email_body)

# Send the email using SMTP
smtp_server = os.environ.get('SMTP_SERVER')
smtp_port = os.environ.get('SMTP_PORT')
smtp_username = os.environ.get('EMAIL_USERNAME')
smtp_password = os.environ.get('EMAIL_PASSWORD')
sender_email = os.environ.get('SENDER_EMAIL')
recipient_email = os.environ.get('RECIPIENT_EMAIL')

with smtplib.SMTP(smtp_server, smtp_port) as smtp:
    smtp.starttls()
    smtp.login(smtp_username, smtp_password)
    message = f'Subject: New release for {repo_name}\n\n{email_body}'
    smtp.sendmail(sender_email, recipient_email, message)
