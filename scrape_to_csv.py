from bs4 import BeautifulSoup
import requests
import csv

csv_file = open('nyt_links.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['link_text', 'link_location']) 

source = requests.get('https://www.nytimes.com')
soup = BeautifulSoup(source.content, 'lxml')
    
story_wrappers = soup.find_all(class_ = 'story-wrapper')
# print(story_wrappers)
    
for item in story_wrappers:
    link_text = item.a.text
    print(link_text)
    
    link_location = item.a['href']
    print(link_location)

    csv_writer.writerow([link_text, link_location])

csv_file.close()