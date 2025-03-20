import os
import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def search_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    titles = [title.text for title in soup.find_all("h1", class_="headline") if (urlparse(url).netloc and (urlparse(url).hostname or urlparse(url).port))]
    return titles

if __name__ == "__main__":
    url = input("Enter the website URL: ")
    results = search_website(url)
    for i, title in enumerate(results, 1):
        print(f"{i}. {title}")
