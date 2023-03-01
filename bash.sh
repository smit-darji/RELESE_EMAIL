releases='[{"name": "v1.0.16", "tag": "v1.0.16", "url": "https://github.com/smit-darji/RELESE_EMAIL/releases/tag/v1.0.16", "body": "v1.0.16"}, {"name": "v1.0.15", "tag": "v1.0.15", "url": "https://github.com/smit-darji/RELESE_EMAIL/releases/tag/v1.0.15", "body": "v1.0.15"}]'

message="New releases available:"

# Use a loop to extract information for each release
for release in $(echo "$releases" | jq -c '.[]'); do
    name=$(echo "$release" | jq -r '.name')
    tag=$(echo "$release" | jq -r '.tag')
    url=$(echo "$release" | jq -r '.url')
    body=$(echo "$release" | jq -r '.body')

    # Add release information to the message
    message+="\n\n$name ($tag)\n$url\n$body"
done

# Print the message
echo -e "$message"