# bs4 tutorial

# welcome

Welcome to this GCDI workshop, "Introduction to Web Scraping with
Python(bs4)"

Please check out our other workshops, consultations, working groups 
on https://gcdi.commons.gc.cuny.edu/

This workshop goes over how to web scrape using python library,
Beautiful Soup 4, or bs4.

In short, bs4 is a Python library for "web scraping," 
or pulling data out of HTML and XML files.

## note on structure

I will be sharing my screen, demonstrating how to do things
you might follow along by watching, or typing as I type
if this topic is very new or confusing, just watch for now.

There will be time for practice in breakout groups

And everything that I type is saved to a file
so you're not going to miss anything

Rafa and Steve are here to help out
Rafa on the chat to answer questions
Steve mostly for aesthetics

Feel free to interrupt as well!

At the beginning e will cover some basics on HTML and CMD Line,
Apologies to those more advanced users, 
But it's necessary to get the most engagement for the group

## what is web scraping

Web scraping is pulling or extracting data from webpages, their HTML files. 

web scraping vs requesting data from APIs
- API - application programming interface, allowing you to talk to an app, request data
- both are about getting data from websites, resources
- except, APIs are created by the data holders, more efficient, with ready JSON, XML
- for example, social media,  weather, sports, financial data, libraries & archives
- Web Scraping is when you pull data directly from the website. Then you convert it
- Web Scraping is more work, more coding, with less support from the source

If there is an API that returns JSON, XML, use that before scraping.

You might find yourself in a scenario where there might not be an API 
to access the data you want, or the access to the API might be too limited 
or expensive.

There are potential legal issues with web scraping if a website doesn't allow it.

## required software

install python and pip 
 
check you have the libraries requests, python
 % pip install requests
 % pip install bs4
 % pip install lxml # parser recommended
 
## software contexts
 
### quick intro what is HTML

sample HTML file
head elements: head, title, h1, h2
body elements: body, a, p
attributes: class, id

### quick intro what is Command Line

% cd, pwd, cd .., cd ~
working in the python shell: entering & exiting

# quick start

## putting the parts together -- bs4 handles HTML data

start an interactive shell
let's see how bs4 engages with html

this is all we need to use bs4: import and soup object
% from bs4 import BeautifulSoup
we have an import statement (only works if it's installed!)
% soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
we have a BS4 object - this takes the source HTML and converts
it into something that we can work with.

now we can print the soup
% print(soup.prettify())
we use the prettify function to make it easier to read

% soup.p # prints paragraph
% soup.b # prints bolded text
% soup.body # prints entire body element
we are using python syntax to acces HTML elements
this is bs4 in a nutshell
 
## final product: how to scrape in 7 lines of code

show you how to scrape a website, in just 7 lines of code
then we will go into detail of how it's done, 
and what we can do with the data

open the NYT website
open up the terminal and activate python shell

import your libraries
% import requests
% from bs4 import BeautifulSoup

use "get" function from requests to access webpage
add webpage as argument here
% webpage = requests.get("URL")

make sure page is accessible
% print(result.status_code) # 200 means success
you can google more about http status codes

% print(result.headers) # prints headers

save all page content to source variable
% source = webpage.content

pass source to BeautifulSoup class, creating soup object,
which we will soon play with
% soup = BeautifulSoup(source, 'lxml')
the lxml is the parser, which you can read more about

print the whole thing, prettily
% soup.prettify()

so overwhelming, how do we know it's NYT? we can search HTML elements
% soup.find('title')

we can also search just the readable text, with function get_text()
% soup.get_text()

# practice time! 

write your own script for a website, using any URL you want.
copy code in chat, or copy from github

# bs4 components

bs4 comes with a set of ready-made python functions for searching HTML
it can search HTML elements ("tags") and attributes
we can look for things in varying amounts of specificity
we can even write our own functions to look for things

## find

we might look for a paragraph
% soup.find('p')
here, we look at the soup object (our content)
run the "find" function, specifying the "p" as param

we can also do the same thing, saving our data to a variable
% paragraph = soup.find('p')
% print(paragraph)
saving to a variable is useful for doing more complex things (you'll see!)

let's look for titles, also saving to variable
% title = soup.find('title')
we have saved the html title element to title variable
% print(title)
we are printing the title variable, containing the whole element, with text

looking for a link
% link = soup.find('a')
% print(link)

another way to write it, without "find":
% soup.a # print first link
% link = soup.a

other elements?
soup.h1
soup.h2
soup.h3

## text & attributes

lets go a little deeper than the element

we can access just the text (getting rid of tags) from elements
% soup.find("p").text
alternatively,
% soup.p.text

% link_text = soup.a
% print(link_text)

we can get the attributes too:
% link_location = link['href']
% print(link_location)

## find_all

% headers = soup.find_all('h3')
the syntax is a function with parameter in parentheses/quotes. 
% print(headers)

% links = soup.find_all('a') # a is the link element
% print(links)

let's say we want a list of the headers, just the text,
and not all the other stuff (tags, ids, classes, etc)
to get a single header, we can run:
% soup.h2.text
but how do we get a list of them?

this doesn't work
% soup.find_all('h3').text
inspect the error - we need to iterate

## looping

in order to do things to a list, we need to iterate over the list
to create a loop

background on loops for those unfamiliar / needing refresher
% for letter in "hello":
    print letter
this goes through each item in the string, and does something
in this case, print
loops are a way to iterate over a list -- do something to each item

% headers = soup.find_all('h3') # create a list of the h3 elements
% headers # returns a list of our h3 elements

the loop - for each item in the list, print the text of that item:
% for item in headers:
     print(item.text)
	 
## scrape_headings.py

let's make this more efficient, let's create a function that grabs all headings
it will loops through the headings in the webpage
and add those headings to a list

def scrape_headings():
    headers = soup.find_all('h3')
    our_headings = []
    for item in headers:
        our_headings.append(item.text)
    print(*our_headings, sep = "\n") # to make separate lines

scrape_headings()

# practice time!

breakout groups

to your script, write a loop so it prints the headlines of nyt

# inspecting pages to access classes

now we are going to learn how to use web browser tools
to help us write scripts for scraping websites.

open up a web browser, go to the website
opening developer tools, under the hood
"inspect element" to see html for webpage -- best tool for scraping

right click, inspect element
check the element for your desired data

on nyt, we see that all of the headlines and text blurbs 
are contained by a class, "story-wrapper"

let's print these, noticing the syntax for "class_"
% soup.find(class_ = "story-wrapper")
here we get the first headline, a rather big clunk of text
containing links, taglines, other elements, etc. 

now let's just get the text
% soup.find(class_ = "story-wrapper").text

cleaner, but what if I wanted to get just the link?

first, create a variable
% story_wrapper = soup.find(class_ = "story-wrapper")
% story_wrapper
returns the entire story_wrapper element, the chuck we saw before

second, to get just the link info, search the "anchor" element
% story_wrapper.a
returns the entire "a" element

third, to get just the link, use syntax for accessing attributes
% story_wrapper.a['href']
the syntax is: tag['attr']; how we get attributes like hyperlink reference
we are accessing it like we access a dictionary in python

finally, search for just the text in "a"
% story_wrapper.a.text

## creating a list to loop through elements by classs

now, we could write ourselves a loop that grabs all of the links from this page
we could also write one that gets just the headlines for the links

let's first create a story_wrapper object,
which contains a list of all story_wrappers on the page
% story_wrappers = soup.find_all(class_ = "story-wrapper")

we have this story_wrappers object now, containing a list
we can write various loops

here is a loop to get just the text
% for item in story_wrappers:
%    print(item.text)

here is a loop to get just text in the anchor tag:
% for item in story_wrappers:
%    print(item.a.text)

getting more specific, just the link location:
% for item in story_wrappers:
%     print(item.a['href']



________________________________________________________
________________________________________________________
# print to csv file

all of this scraping is great, but we should also think about
way to work with the data we create
in order to do that, we need to save the data to a workable format

let's save the output from our web scraping to a CSV format
comma separated values -- spreadsheet

first, install csv
```
% pip install csv
```

then we create a new script, let's name it scrape_to_csv.py
with the following two lines:

```python

from bs4 import BeautifulSoup
import requests
import csv

csv_file = open('nyt_links.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['link_text', 'link_location']) 

source = requests.get('https://www.nytimes.com')
soup = BeautifulSoup(source.content, 'lxml')
    
story_wrappers = soup.find_all(class_ = 'story-wrapper')
    
for item in story_wrappers:
    link_text = item.a.text
    print(link_text)
    
    link_location = item.a['href']
    print(link_location)

    csv_writer.writerow([link_text, link_location])

csv_file.close()
```
	
After running this file in the terminal, we should see
the output in our present working directory.

Open the file to check that we have the correct output.

AND THAT'S IT!

You have now learned the basic steps of pulling data, 
organizing it, and saving it. 

The next steps is to analyze that data. 
For that, you have several choices, such as
text analysis with NLTK (natural langauge toolkit), 
or data analysis with pandas (python data anlaysis & manipulation),
which are not covered in this workshop.

But we do have resources on these!
Check out our other workshops:

![Text Analysis with NLTK workshop](https://curriculum.dhinstitutes.org/workshops/text-analysis/)

![Data Analysis with Pandas workshop](https://digitalfellows.commons.gc.cuny.edu/2021/04/09/exploring-data-with-python-and-pandas/)

# sources

![Beautiful Soup 4 docs](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

![Beautiful Soup 4 on PiPy](https://pypi.org/project/beautifulsoup4/)

![Corey's Schafer's YouTube tutorial, from html to csv](https://www.youtube.com/watch?v=ng2o98k983k)

![Real Python's web scrapping with bs4 tutorial](https://realpython.com/python-web-scraping-practical-introduction/)

# next steps

Here are some other tutorials specifically for web scraping social media. 

![Scraping reddit into JSON format](https://www.scrapehero.com/a-beginners-guide-to-web-scraping-part-2-build-a-scraper-for-reddit/). 
Script (with walkthrough) on how to scrape data from Reddit. 
Although reddit also has a handy ![api](https://www.reddit.com/dev/api/). 

![Instagram-scraper](https://github.com/arc298/instagram-scraper). 
Module for scraping instagram that outputs automatically into JSON file. 
