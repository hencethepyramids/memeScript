import requests
import random
import webbrowser

# Define the URL of the "imgflip.com" API to fetch memes
api_url = 'https://api.imgflip.com/get_memes'

# Send an HTTP GET request to the API
response = requests.get(api_url)

# Check if the request was successful
if response.status_code == 200:
    print("HTTP request successful")
    
    # Parse the JSON content of the response
    meme_data = response.json()
    
    # Extract the list of memes from the data
    memes = meme_data.get('data', {}).get('memes', [])

    if memes:
        print("Memes found")

        # Choose a random meme from the list
        random_meme = random.choice(memes)

        # Get the meme's image URL
        meme_url = random_meme['url']

        # Display the meme in a web browser
        webbrowser.open_new_tab(meme_url)

        print(f'Fetched and opened a random meme in your default web browser.')
    else:
        print('No memes found in the API response.')
else:
    print('Failed to fetch memes from the API.')

# Remember to handle exceptions, error handling, and customize for your specific use case.
