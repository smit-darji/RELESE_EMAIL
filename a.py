import os
import requests
from datetime import datetime, timedelta

def get_release_data():
    api_url = "https://api.github.com/repos/{owner}/{repo}/releases"
    owner = os.environ["GITHUB_REPOSITORY_OWNER"]
    repo = os.environ["GITHUB_REPOSITORY_NAME"]
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}"
    }
    today = datetime.utcnow().date()
    week_ago = today - timedelta(days=7)
    params = {
        "per_page": 100,
        "page": 1,
        "since": week_ago.isoformat()
