import requests
from bs4 import BeautifulSoup

# Get the HTML of the website
url = 'https://www.walmart.com/'
response = requests.get(url)

# Parse the HTML with Beautiful Soup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the elements you want to scrape
title = soup.find('title').text
links = soup.find_all('a')

# Print the title and links
print(title)
for link in links:
    print(link.text, ":", link['href'])
    print(link)