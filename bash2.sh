releases='[
  {
    "name": "v1.0.6",
    "tag": "v1.0.6",
    "url": "https://github.com/smit-darji/RELESE_EMAIL/releases/tag/v1.0.6",
    "body": "sdsadsd"
  },
  {
    "name": "v1.0.4",
    "tag": "v1.0.4",
    "url": "https://github.com/smit-darji/RELESE_EMAIL/releases/tag/v1.0.4",
    "body": "sadadasdsad"
  },
  {
    "name": "v1.0.3",
    "tag": "v1.0.3",
    "url": "https://github.com/smit-darji/RELESE_EMAIL/releases/tag/v1.0.3",
    "body": "asdsadsadad"
  },
  {
    "name": "v1.0.2",
    "tag": "v1.0.2",
    "url": "https://github.com/smit-darji/RELESE_EMAIL/releases/tag/v1.0.2",
    "body": "sadadadad"
  },
  {
    "name": "v1.0.1",
    "tag": "v1.0.1",
    "url": "https://github.com/smit-darji/RELESE_EMAIL/releases/tag/v1.0.1",
    "body": "asdadadada"
  },
  {
    "name": "v1.0.0",
    "tag": "v1.0.0",
    "url": "https://github.com/smit-darji/RELESE_EMAIL/releases/tag/v1.0.0",
    "body": "asdadad"
  }
]'

all_messages=""

for release in $(echo "$releases" | jq -c '.[]'); do
    name=$(echo "$release" | jq -r '.name')
    tag=$(echo "$release" | jq -r '.tag')
    url=$(echo "$release" | jq -r '.url')
    body=$(echo "$release" | jq -r '.body')    
    message="Release $name ($tag) is now available. Download it from ($url)}.\n Description is :$body\n\n"
    
    all_messages="$all_messages$message" 
done

echo -e "$all_messages"


