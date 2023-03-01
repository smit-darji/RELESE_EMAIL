releases='[
  {
    "name": "v1.0.16",
    "tag": "v1.0.16",
    "url": "https://github.com/smit-darji/RELESE_EMAIL/releases/tag/v1.0.16",
    "body": "v1.0.16"
  },
   {
    "name": "hey this is demo of v1.0.8",
    "tag": "v1.0.8",
    "url": "https://github.com/smit-darji/RELESE_EMAIL/releases/tag/v1.0.8",
    "body": "helolo this is demo of v1.0.8"
  },
  {
    "name": "v1.0.15",
    "tag": "v1.0.15",
    "url": "https://github.com/smit-darji/RELESE_EMAIL/releases/tag/v1.0.15",
    "body": "v1.0.15"
  },
  {
    "name": "v1.0.14",
    "tag": "v1.0.14",
    "url": "https://github.com/smit-darji/RELESE_EMAIL/releases/tag/v1.0.14",
    "body": ""
  },
  {
    "name": "v1.0.13",
    "tag": "v1.0.13",
    "url": "https://github.com/smit-darji/RELESE_EMAIL/releases/tag/v1.0.13",
    "body": "v1.0.13"
  },
  {
    "name": "v1.0.12",
    "tag": "v1.0.12",
    "url": "https://github.com/smit-darji/RELESE_EMAIL/releases/tag/v1.0.12",
    "body": "v1.0.12"
  },
  {
    "name": "v1.0.11",
    "tag": "v1.0.11",
    "url": "https://github.com/smit-darji/RELESE_EMAIL/releases/tag/v1.0.11",
    "body": "v1.0.11"
  },
  {
    "name": "v1.0.9",
    "tag": "v1.0.9",
    "url": "https://github.com/smit-darji/RELESE_EMAIL/releases/tag/v1.0.9",
    "body": "v1.0.9 nthis is main relese of weekl"
  },
  {
    "name": "hello this is : v1.0.7",
    "tag": "v1.0.7",
    "url": "https://github.com/smit-darji/RELESE_EMAIL/releases/tag/v1.0.7",
    "body": "hello this is v1.0.7"
  },
  {
    "name": "v1.0.6",
    "tag": "v1.0.6",
    "url": "https://github.com/smit-darji/RELESE_EMAIL/releases/tag/v1.0.6",
    "body": ""
  },
  {
    "name": "v1.0.5",
    "tag": "v1.0.5",
    "url": "https://github.com/smit-darji/RELESE_EMAIL/releases/tag/v1.0.5",
    "body": ""
  },
  {
    "name": "v1.0.4",
    "tag": "v1.0.4",
    "url": "https://github.com/smit-darji/RELESE_EMAIL/releases/tag/v1.0.4",
    "body": ""
  },
  {
    "name": "v1.0.3",
    "tag": "v1.0.3",
    "url": "https://github.com/smit-darji/RELESE_EMAIL/releases/tag/v1.0.3",
    "body": ""
  },
  {
    "name": "v1.0.2",
    "tag": "v1.0.2",
    "url": "https://github.com/smit-darji/RELESE_EMAIL/releases/tag/v1.0.2",
    "body": ""
  },
  {
    "name": "v1.0.1",
    "tag": "v1.0.1",
    "url": "https://github.com/smit-darji/RELESE_EMAIL/releases/tag/v1.0.1",
    "body": ""
  },
  {
    "name": "relese v1.0.0",
    "tag": "v1.0.0",
    "url": "https://github.com/smit-darji/RELESE_EMAIL/releases/tag/v1.0.0",
    "body": ""
  }
]'


message=""

for release in $(echo "$releases" | jq -c '.[]'); do
    name=$(echo "$release" | jq -r '.name')
    tag=$(echo "$release" | jq -r '.tag')
    url=$(echo "$release" | jq -r '.url')
    body=$(echo "$release" | jq -r '.body')
    message="Release :$name  $tag is now available. Download it from  $url ,and description is :$body"
    echo "$message"
done

# # Print the message
