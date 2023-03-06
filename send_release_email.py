import os
import requests
from datetime import datetime, timedelta
from jinja2 import Environment, FileSystemLoader

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

# Define the start and end dates for the release query
end_date = datetime.now()
start_date = end_date - timedelta(days=7)

# Query the GitHub API for releases in the last week
response = requests.get(
    f'{api_url}/repos/smit-darji/RELESE_EMAIL/releases',
    headers=auth_header
)

# Filter the releases by date
releases = [
    release for release in response.json()
    if start_date <= datetime.fromisoformat(release['published_at'][:-1]) <= end_date
]

# Render the email template using Jinja2
template = env.get_template('release_email_template.j2')
email_body = template.render(repo_owner="smit-darji", repo_name="RELESE_EMAIL", releases=releases)

# Output the email body
print(email_body)
os.environ['email_body'] = email_body

print(f"::set-output name=demo::{email_body}")
