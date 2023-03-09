import requests

owner = "smit-darji"
repo = "RELESE_EMAIL"# replace with the name of the repository
url = f'https://api.github.com/repos/{owner}/{repo}/releases/latest'

response = requests.get(url)
if response.status_code == 200:
    release = response.json()
    print(f"The latest release is {release['name']} ({release['tag_name']})")
else:
    print(f"Failed to retrieve latest release. Error code: {response.status_code}")