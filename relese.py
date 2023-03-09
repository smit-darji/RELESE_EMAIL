import requests
import os

# Define the repository details
repo_name = "smit-darji"
repo_owner = "RELESE_EMAIL"

# Define the GitHub API endpoint
api_url = f'https://api.github.com/repos/smit-darji/RELESE_EMAIL/releases/latest'

# Set up the authentication headers
auth_header = {
    'Authorization': f'token {os.environ.get("GITHUB_TOKEN")}',
    'Accept': 'application/vnd.github.v3+json'
}

# Query the GitHub API for the latest release
response = requests.get(api_url, headers=auth_header)

# Check if the request was successful
if response.status_code == requests.codes.ok:
    # Extract the relevant details from the response
    release_data = response.json()
    release_tag = release_data['tag_name']
    release_name = release_data['name']
    release_body = release_data['body']
    
    # Print the release details
    print(f'Latest release: {release_name} ({release_tag})')
    print(f'Release notes: {release_body}')
else:
    # Print an error message
    print(f'Error: {response.status_code} - {response.text}')
