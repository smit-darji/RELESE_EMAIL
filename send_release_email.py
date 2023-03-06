from github import Github
from jinja2 import Template

# Create a Github instance
g = Github()

# Get a repository by its owner and name
repo = g.get_repo("smit-darji/RELESE_EMAIL")

# Get the latest release
latest_release = repo.get_latest_release()

# Format the release details as a string
release_details = f"Release name: {latest_release.title}\nRelease tag: {latest_release.tag_name}\nRelease body: {latest_release.body}"
template = Template("{{ release_details }}")

# Render the template with the release details
email_body = template.render(release_details=release_details)
print(email_body)