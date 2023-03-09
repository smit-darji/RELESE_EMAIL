import os
import ssl
import requests
import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Define the repository owner and name
owner = "smit-darji"
repo = "RELESE_EMAIL"

# Define the start and end dates for the search range (last 7 days)
end_date = datetime.datetime.now()
start_date = end_date - datetime.timedelta(days=7)

# Make a GET request to the GitHub API to retrieve the releases
api_url = 'https://api.github.com'
github_token="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"
auth_header = {
    'Authorization': f'token {github_token}',
    'Accept': 'application/vnd.github.v3+json'
}

response = requests.get(
    f'{api_url}/repos/smit-darji/RELESE_EMAIL/releases/latest',
    headers=auth_header
)

if response.status_code != 200:
    raise Exception(f"Failed to retrieve releases. Error code: {response.status_code}")
url = f"https://api.github.com/repos/smit-darji/RELESE_EMAIL/releases"
response = requests.get(url)

# Check if the response was successful
if response.status_code != 200:
    raise Exception(f"Failed to retrieve releases. Error code: {response.status_code}")

# Parse the response to extract the relevant information for each release
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

# Check if there are any releases within the specified time range
if not releases:
    print("No releases in the last week.")
else:
    # Define the email parameters
    sender_email = "smit.softvan@gmail.com"
    recipient_email = "sahilvandra.softvan@gmail.com"
    password = "Softvan@smit1"
    subject = f"New releases for {owner}/{repo}"
    
    # Create the email message body with details of the releases
    body = "<h2>New releases:</h2>"
    for release in releases:
        body += f"<h3>{release['name']}</h3>"
        body += f"<p>Tag: {release['tag_name']}</p>"
        body += f"<p>Published at: {release['published_at']}</p>"
        body += f"<p>URL: {release['url']}</p>"
        body += f"<p>{release['body']}</p>"
    
    # Create the email message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "html"))
    
    print(message.as_string())
    smtp_server = "smtp.gmail.com"
    port = 587  # for starttls
    sender_email = "smit.softvan@gmail.com"
    password = "qmkbtqileavaxwnq"
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls(context=context)
        server.login(sender_email, password)
        
        # send the message
        message = "Subject: Hi there!\n\nThis is a test message."
        recipient_email = "sahilvandra.softvan@gmail.com"
        server.sendmail(sender_email, recipient_email, message)

    print("Email sent successfully!", )
