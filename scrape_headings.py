from bs4 import BeautifulSoup
import requests
import lxml

webpage = requests.get('https://www.nytimes.com')
source = webpage.content
soup = BeautifulSoup(source, 'lxml')

def scrape_headings():
    headers = soup.find_all('h3')
    our_headings = []
    for item in headers:
        our_headings.append(item.text)
    print(*our_headings, sep = "\n") # to make separate lines

scrape_headings()