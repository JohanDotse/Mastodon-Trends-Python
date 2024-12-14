import requests

# URL of the Mastodon API for trending tags
url = 'https://mastodon.social/api/v1/trends/tags'

# Send GET request to the API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse JSON response
    trends = response.json()

    # Open a file in write mode
    with open('tags.txt', 'w') as file:
        # Iterate through trending tags
        for tag in trends:
            tag_name = tag['name'].lower()  # Convert tag name to lowercase
            print(tag_name)  # Print to the screen
            file.write(tag_name + '\n')  # Write to the file
else:
    print(f"Failed to retrieve data: {response.status_code}")
