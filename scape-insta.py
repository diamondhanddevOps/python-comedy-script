import requests
import csv
from bs4 import BeautifulSoup

def scrape_skit_videos():
    # Set the URL you want to scrape
    url = 'https://www.instagram.com/explore/tags/skitvideosinnigeria/'

    # Make a GET request to the website
    response = requests.get(url)

    # Parse the HTML of the webpage
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all the div elements with the class 'v1Nh3'
    skit_videos = soup.find_all('div', {'class': 'v1Nh3'})

    # Create a new CSV file to store the data
    with open('skit_videos.csv', 'w') as csv_file:
        # Use csv.writer to write the rows
        writer = csv.writer(csv_file)
        # Write the header row
        writer.writerow(['Link', 'Caption'])
        
        # Loop through all the skit videos
        for skit_video in skit_videos:
            # Find the link to the video
            link = skit_video.find('a')['href']
            # Find the caption for the video
            caption = skit_video.find('div', {'class': 'C4VMK'}).text
            # Write the data to the CSV file
            writer.writerow([link, caption])

scrape_skit_videos()
git