releases='[
    { "name": "v1.0.6", "url": "https://github.com/smit-darji/RELESE_EMAIL/releases/tag/v1.0.6", "published_at": "2023-03-01T06:10:24Z" },
    { "name": "v1.0.4", "url": "https://github.com/smit-darji/RELESE_EMAIL/releases/tag/v1.0.4", "published_at": "2023-03-01T06:00:49Z" },
    { "name": "v1.0.3", "url": "https://github.com/smit-darji/RELESE_EMAIL/releases/tag/v1.0.3", "published_at": "2023-03-01T05:59:55Z" },
    { "name": "v1.0.2", "url": "https://github.com/smit-darji/RELESE_EMAIL/releases/tag/v1.0.2", "published_at": "2023-03-01T05:57:48Z" },
    { "name": "v1.0.1", "url": "https://github.com/smit-darji/RELESE_EMAIL/releases/tag/v1.0.1", "published_at": "2023-03-01T05:52:37Z" }
]'
body=""
for release in $(echo "$releases" | jq -c '.[]'); do
    name=$(echo $release | jq -r '.name')
    tag=$(echo $release | jq -r '.tag')
    url=$(echo $release | jq -r '.url')
    published_at=$(echo $release | jq -r '.published_at')
    formatted_date=$(date -d $published_at +'%Y-%m-%d %H:%M:%S')
    message="New version is Release :$name  \nyou can Show at : $url. \nrelese Date is :$formatted_date.\n\n"
    body="$body$message"
done
echo $body >> a.txt
file_contents=$(cat a.txt)
echo "$file_contents"
rm a.txt
