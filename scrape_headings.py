from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.nytimes.com')
soup = BeautifulSoup(source.content, 'lxml')

def scrape_headings():
    headers = soup.find_all('h3')
    our_headings = []
    for item in headers:
        our_headings.append(item.text)
    print(*our_headings, sep = "\n") # to make separate lines

scrape_headings()