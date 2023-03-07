import os
import requests
from jinja2 import Environment, FileSystemLoader
import smtplib

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

# Query the GitHub API for the latest release
response = requests.get(
    f'{api_url}/repos/smit-darji/RELESE_EMAIL/releases/latest',
    headers=auth_header
)

# Get the details of the latest release (if there are any releases
release = response.json()
name = release['name']
tag = release['tag_name']
url = release['html_url']
body = release['body']

# Render the email template using Jinja2
template = env.get_template('release_email_template.j2')
email_body = template.render(repo_owner="smit-darji", repo_name="RELESE_EMAIL", name=name, tag=tag, url=url, body=body)

# Output the email body
print(email_body)
os.environ['demo'] = email_body

# Send the email
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("smit.softvan@gmail.com", "wkyjrlcyhsvajarh")
s.sendmail("smit.softvan@gmail.com", "sahilvandra.softvan@gmail.com", email_body)
s.quit()
