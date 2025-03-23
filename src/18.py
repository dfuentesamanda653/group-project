import requests
from bs4 import BeautifulSoup
import re

def scrape_data(url):
    # Send GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all div elements with class "title" and "tag"
        titles = soup.find_all('div', {'class': 'title'})
        tags = soup.find_all('div', {'class': 'tag'})
        
        # Extract data from the found elements
        for title in titles:
            print(f"Title: {title.text}")
        
        for tag in tags:
            print(f"{re.sub(r'\s+', ' ', tag.text).strip()}")
    else:
        print("Failed to retrieve data")

# Example usage
url = "https://www.example.com"
scrape_data(url)
