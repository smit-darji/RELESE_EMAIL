releases='[{"name": "v1.0.16", "tag": "v1.0.16", "url": "https://github.com/smit-darji/RELESE_EMAIL/releases/tag/v1.0.16", "body": "v1.0.16"}, {"name": "v1.0.15", "tag": "v1.0.15", "url": "https://github.com/smit-darji/RELESE_EMAIL/releases/tag/v1.0.15", "body": "v1.0.15"}]'


message=""

# for release in $(echo "${releases}" | jq -r '.[] | @base64'); do
#     # Decode the release JSON data
#     _jq() {
#      echo ${release} | base64 --decode | jq -r ${1}
#     }
    
#     # Create a message for the release
#     message="Release ${_jq '.name'} (${_jq '.tag'}) is now available. Download it from ${_jq '.url'}."

#     # Print the message
#     echo "${message}"
# done
# Use a loop to extract information for each release
for release in $(echo "$releases" | jq -c '.[]'); do
    name=$(echo "$release" | jq -r '.name')
    tag=$(echo "$release" | jq -r '.tag')
    url=$(echo "$release" | jq -r '.url')
    body=$(echo "$release" | jq -r '.body')
    message="Release :$name  $tag is now available. Download it from  $url ,and description is :$body"
    echo "$message"
done

# # Print the message
