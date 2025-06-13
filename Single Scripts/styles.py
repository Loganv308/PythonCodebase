import requests
from bs4 import BeautifulSoup

# Get the HTML of the website
url = 'https://www.amazon.com/'
response = requests.get(url)

# Parse the HTML with Beautiful Soup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the CSS style sheet
css_link = soup.find('link', attrs={'rel': 'stylesheet'})

# Get the URL of the CSS style sheet
css_url = css_link['href']

# Download the CSS style sheet
css_content = requests.get(css_url).content

# Save the CSS style sheet to a file
with open(f'{url}.css', 'wb') as f:
    f.write(css_content)
    print(f, "written...")

