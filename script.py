import requests
from bs4 import BeautifulSoup
import random
import webbrowser

# Define the URL of the website where you want to fetch memes
url = 'https://www.memedroid.com/memes/random'

# Send an HTTP GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all image elements on the page (customize this based on the website structure)
    images = soup.find_all('img')

    # Filter images to select memes based on your criteria
    memes = [img for img in images if 'meme' in img.get('alt', '').lower()]

    if memes:
        # Choose a random meme from the list
        random_meme = random.choice(memes)

        # Get the meme's image URL
        meme_url = random_meme['src']

        # Display the meme in a web browser
        webbrowser.register('opera', None, webbrowser.BackgroundBrowser("C:\\Users\\ethan\\AppData\\Local\\Programs\\Opera GX\\launcher.exe"))
        webbrowser.get('opera').open_new_tab(meme_url)

        print(f'Fetched and opened a random meme in your default web browser.')
    else:
        print('No memes found on the page.')
else:
    print('Failed to fetch the website.')

# Remember to handle exceptions, error handling, and customize for your specific use case.
