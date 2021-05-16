# bs4 tutorial

# welcome

Welcome to this GCDI workshop, "Introduction to Web Scraping with
Python(bs4)"

## GCDI

This workshop is sponsored by the Graduate Center Digital Initiatives, and in particular, the Digital Fellows. GCDI offers different kinds of support for digital scholarship in the GC. Some of the more popular resources we offer are regular workshops (like this one), consultations, working groups based around common tools or data sources (such as python, R, mapping, digital archives, sound studies, data visualization), special events (check our calendar!) and online resources.

Some ways to get involved:
- Sign up for a [consultation](https://docs.google.com/forms/d/e/1FAIpQLSeLEski53U3FjArac-bVU0jYwxYD0HQTvNSQUxIZWoxbqDPWg/viewform) to speak to a fellow about your digital project.
- Check the Event Calendar for upcoming events and workshops: cuny.is/workshops
- Follow GCDI or the Digital Fellows on Twitter: [@cunygcdi](https://twitter.com/cunygcdi) and [digital_fellows](https://twitter.com/digital_fellows).
- Follow (and post to!) the [#digitalGC](https://twitter.com/search?q=%23digitalgc&src=typed_query) hashtag on Twitter
- Join the GCDI Group on the CUNY Academic Commons for all GCDI-related updates! cuny.is/group-gcdi

Please check out our other workshops, consultations, working groups 
on https://gcdi.commons.gc.cuny.edu/

# bs4

This workshop goes over how to web scrape using python library, Beautiful Soup 4, or bs4.

In short, bs4 is a Python library for "web scraping," or pulling data out of HTML and XML files. It allows people to take information, including text and images, from websites. It's often used for taking all kinds of data, like news, financial, sports, social media data. Once we take this data, we usually put it into a format like JSON or CSV (spreadsheet) for further analysis. 

In this workshop, we will be using bs4 to scrape news data from the New York Times website. By this end of this workshop, you will have a python script that can grab data from a website and export that data into a CSV file. Then, at the very end, I will show you a couple of other ways to scrape websites, that go beyond bs4, for scraping social media. 

Throughout the workshop, we will:
- discuss Web Scraping, distinguishing it from other data gathering methods like APIs
- quickly review the basics of HTML (for those who need a refresher)
- jump into using bs4 for exploring web pages; learning about various functions and methods for bs4, going into some specificity. 
- learn to write scripts in bs4 to automate searching for website data, and to export our scraped data to csv files (spreadsheets)
- explore web wbrowser tools (the inspector) for identifying elements to scrape from websites

The main point of the workshop is not to make you an expert at web scraping, but to teach you enough that you can continue to learn on your own, and begin your own webscraping projects. 

This workshop assumes basic familiarity with python, HTML, and the command line. In the case that you do *not* have this knowledge, I highly recommend reading through these GC Digital Humanities Research Institute materials:

- DHRI workshop on [the Command Line](https://curriculum.dhinstitutes.org/workshops/command-line/) (complete lessons 1-6, through "Navigation")
- DHRI workshop on [HTML/CSS](https://curriculum.dhinstitutes.org/workshops/html-css/) (complete lessons 1-6, through "Links")
- DHRI workshop on [Python](https://curriculum.dhinstitutes.org/workshops/python/) (complete lessons 1-7, through "Loops")

## note on structure

I will be sharing my screen, demonstrating how to do things. You might follow along by watching, or typing as I type. However, if this topic is very new or confusing, I strongly recommend that you just watch for now. If you are not comfortable with Python, you will likely get errors if you try to type as I type, which can be frustrating. 

There will be time for you to practice--I've structured practice time into the session. You will have a few minutes to replicate what I'm doing before we move on.

And do not worry about falling behind, all of the code that I type is saved to a separate file (this one!), so you're not going to miss anything.

Rafa and Steve are here to help out. Rafa will be on the chat to answer questions; Steve will just be his regular helpful self. If you have any questions, please put them in the chat, or feel free to speak up and interrupt me as well.

Let's get started. 

## what is Web Scraping?

Web scraping is pulling or extracting data from webpages. 

In the most simple explanation, Web Scraping is going into a website, and pulling the information from those websites. This data is in the form of HTML files.

## what is bs4? 

bs4 is short for `Beautiful Soup 4`, a python package that allows us to work with HTML data. In very abstract terms, bs4 uses python syntax to access HTML objects. In more familiar terms, this means that we are using the python language and its way of asking information from pages written in the web's main computer lanugage, HTML.

### Web Scraping vs using APIs
- API - application programming interface - a software that allows you to talk to an app, to request data from that app, which it delivers to you
- both web scraping and API are about getting data from websites
- except, APIs are created by the data holders, more efficient, with ready JSON, XML. Can include social media,  weather, sports, financial data, libraries & archives. For example Reddit, Twitter, New York Public Library, the Metropolitan Museum of Art, SkyScanner, etc, all have APIs.
- web scraping is more work, more coding, with less support from the source. Web Scraping is when you pull data directly from the website. Then you convert it. 

### some advice:

If there is an API that returns JSON, XML, use that before scraping. 

You might find yourself in a scenario where there might not be an API to access the data you want, or the access to the API might be too limited  or expensive. In this case, web scraping might be your best route. 

There are potential legal issues with web scraping if a website doesn't allow it.

## required software

Install python. Click here to install our recommended python distribution, [Anaconda](https://www.anaconda.com/products/individual). Scroll to the bottom of the page, and click the relevant version for your machine. This part might take a few minutes, so be patient. 
 
Once you have python, let's check you have the rest of the python packages: `requests` (for requesting data over the web), `bs4` (the beautiful soup 4 package), and `lxml` (the recommended parser for bs4).

Open up your terminal (or gitbash, powershell in windows) and type the following:

```console
% pip install requests
% pip install bs4
% pip install lxml
```

## HTML refresher

Just as a refresher, I'm going to examine a sample HTML file. We will be paying attention to **head** elements, including the **title**, **h1**, **h2** tags, and the **body** elements, including **a** and **p** tags, as well as some attributes like **class** and **href**. 

This is the basic structure of the HTML document, which tells the computer how to layout the web page. 

```html
<html>
    <head>
        <title>The Dormouse's story</title>
        <h1>This is a first level heading</h1>
        <h2>This is a second level heading</h2>
    </head>
    <body>
        <p class="title"><b>The Dormouse's story</b></p>
        <p class="story">Once upon a time there were three little sisters; and their names were
        <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
        <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
        <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
        and they lived at the bottom of a well.</p>
        <p class="story">...</p>
    </body>
</html>
```

If this looks overwhelming to you, make sure you check out the HTML workshop linked above. 

# quick start: exploring bs4

To begin playing around with bs4, let's start a python interactive session on our Terminal (or gitbash, powershell if you are on Windows):

```console
% python
```

Once we get a result like below, we know we are in the interactive mode. Make sure the Python version is Python 3; if it's Python 2, then you should follow the above steps to download Anaconda. 

```console
% python
Python 3.7.7 (default, May  6 2020, 04:59:01) 
[Clang 4.0.1 (tags/RELEASE_401/final)] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

If this is confusing for you, make sure you check out the Command Line tutorial above.

Now we have an interactive shell, let's see jump into bs4 to see what we can do. First, we will import the package, then we will create a beautiful soup object. Inside that object, we will include some HTML.

```console
>>> from bs4 import BeautifulSoup
>>> soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
```
Our bs4 object takes the source HTML and converts it into something that we can work with.

Now we can print the soup, using the `print` funciton, and make it easier to read, using the `prettify()` function. 

```console
>>> print(soup.prettify())
```

Here we see the basic HTML structure, with head, bold, paragraph tags. Beautiful soup creates this `soup` object which parses the HTML data into this tree structure. In programmy terms, we've created a beautiful soup object `soup` which contains attributes (or information) like `p` for paragraph, `b` for bold, and `body` for body. 

This word "object" in Python is something you'll hear often. It means a collection of data and functions that can work on that data. You can think of it as a way of representing real world objects (like this story) in a way that is organized and accessible, so you can work with that information, with Python. 

Let's take an initial look into what this beautiful soup object can do. It takes the HTML source, the specific HTML elelements or "tags," and makes it possible for us to access those tags using python syntax. 

```console
>>> soup.i
>>> soup.b
>>> soup.p
```

Using python syntax to access HTML elements is beautiful soup in a nutshell. 
 
## how to scrape a webpage in 6 lines of code

One of the more impressive things about beautiful soup is how much it can do with just a few lines of code. We can scrape an entire webpage, for example. 

I'll show you how it's done with the [New York Times](https://www.nytimes.com/) website.

First, activate your python shell. Then import your packages. Afterward, we have three lines of code that grab and save website data, and create a beautiful soup object which we can query.  

```console
>>> import requests
>>> from bs4 import BeautifulSoup
>>> import lxml

>>> webpage = requests.get("https://www.nytimes.com")
>>> source = webpage.content
>>> soup = BeautifulSoup(source, 'lxml')
```

For the `webpage` variable, we use the `get()` function from requests to access the webpage. The webpage URL is the parameter here (the thing in parenthesis). 

Then, we save all page content to source variable in the `source` variable.

Finally, we pass `source` to the `BeautifulSoup` class, along with `'lxml'`, to create the soup object.

Let's pause for a second. At this point, you may get an error. Especially happens when you are trying to type something word for word, when you might make a mistake. Below is an example of an error when creating the `soup` object and calling `BeautifulSoup`:

```console
>>> soup = beautifulsoup(source, 'lxml')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'beautifulsoup' is not defined
>>> 
```

This error gives us an insight into what's going on. Check the error message: `name 'beautifulsoup' is not defined` which tells us that python doesn't recognize the line of code. This means we are probably typing something wrong, and we are. In this case we forgot to capitalize the "B" and "S" in beautiful soup, which is necessary since that's the syntax for writing python classes (and BeautifulSoup is a class). 

### the Beautiful Soup object

Once we fix the errors, we can start to look at this `BeautifulSoup` object, the `soup`, which we created. Again, an object is a collection of data and functions that we can use Python to access and manipulate. It represents a real world thing, in this case, the front page of the New York Times. 

We can print the entire thing (the `soup` object) in our terminal with one more line of code, which includes the `prettify()` function.

```console
>>> soup.prettify()
```

This is pretty overwhelming, because it's the entire source HTML for the front page of the New York Times. But there are other ways we can access the elements with specificity. 

We can get the webpage title:

```console
>>> soup.find('title')
```

We can also search just the readable text, getting rid of all the html tags:

```console
>>> soup.get_text()
```

### a note on Python syntax

Here you'll notice that there are multiple ways for accessing the `soup` object in Python. The Python syntax offers us a few options. For example, We might use the `find()` function, to access the title, like `soup.find('title')`, or we can access the title attribute, using dot syntax, like `soup.title`. 

See how the two different syntax examples return the same result?

```console
>>> soup.find('title')
<title data-rh="true">The New York Times - Breaking News, US News, World News and Videos</title>
>>> soup.title
<title data-rh="true">The New York Times - Breaking News, US News, World News and Videos</title>
```

The difference between the two is the difference between functions and attributes. It's not super important now, though it can be as you write more complex python expressions and scripts. 

## practice time! 

Now take a few minutes to try replicating this process in your terminal. Write your own script for a website, using any URL you want.

Practice accessing attributes like `title` and using functions like `get_text()` and `prettify()`.

In the meantime, feel free to interrupt or ask questions here or in the chat. 

# bs4 components

As you are starting to see, beautiful soup comes with a set of custom python functions for searching HTML. It can search HTML tags like `<p>` and attributes like `href`. We can use it look for things in varying amounts of specificity. We can even write our own functions to look for things.

Let's explore the most used function for bs4.

## find()

The `find()` function allows us to... find things! 

We might use it to search for a paragraph:

```console
>>> soup.find('p')
```

Here, we look at the soup object (our content), run the `find()` function, specifying the `p` as param, which goes within parentheses. 

We can also do the same thing while saving the output to a variable.

```console
>>> paragraph = soup.find('p')
>>> print(paragraph)
```

Saving the output to a variable is useful for doing more complex things (you'll see!).

Let's look for titles, also saving to variable:

```console
>>> title = soup.find('title')
>>> print(title)
```

Note that the output prints the title variable, containing the whole element, with text.

Now, let's look for a link, using the `a` tag:

```console
>>> link = soup.find('a')
>>> print(link)
```

Just to practice, let's use the dot syntax, rather than the `find()` function:

```console
% soup.a # print first link
% link = soup.a
```

The dot syntax is shorter to type and can be really useful for quick little seraches. Let's take a look to see wat other elements we can access on this page.

```console
>>> soup.h1
>>> soup.h2
>>> soup.h3
```

We see that most of the important headlines are in the `h3` element, which will be useful for later when we want to pull out these headlines from the HTML.

## .text

Fist, let's go a little deeper than the element. We can access just the text (getting rid of tags like `<p>` or `<h3>` ) from elements.

```console
>>> soup.p.text
```

Here we see just the text, so everything that being is wrapped by HTML elements.

We can do it with links too, while saving it to a variable:

```console
>>> soup.a.text
```

Let's save the link text to a variable, `link_text`:

```console
>>> link_text = soup.a.text
>>> print(link_text)
```

## ['href']

In addition to text, we can also get the attributes. Attributes are additional data that is contained within the HTML tag, like `href`, which stands for hyperlink reference. This is the link's URL. To access the attributes like `href`, we use the syntax: `tag['attr']`.

```console
>>> soup.a['href']
```

Here, the syntax uses square brackets and single quotes to get `href`, which is the same syntax that we use to get values from python dictionaries. 

Let's save the href attribute to a variable. 

```consle
>>> link_location = soup.a['href']
>>> print(link_location)
```

## find_all()

Want to print out all tags of a specific element? Then we use `find_all()`

```console
>>> soup.find_all('h3')
```

Taking a closer look at the output, notice that we have a python `list` object, which consists of a list of items separated by commas, contained withing square brackets. This kind of object is going to be important soon, when we start to look at looping over lists. 

Let's set the level 3 headers to a variable called `headers`. Remember, the syntax is a function with parameter in parentheses/quotes. 

```console
>>> headers = soup.find_all('h3')
>>> print(headers)
```

Let's try with links:

```console
>>> links = soup.find_all('a')
>>> print(links)
```

That's a whole lot of data! Don't worry, we will deal with it soon. 

For now, let's say we want a list of the headers, just the text of the header, and not all the other stuff (tags, ids, classes, etc). To get a single header, we can run:

```console
>>> soup.h3.text
```

But how do we get a list of the headers? You think `soup.find_all('h3').text` would be the correct syntax, but it gets an error. Let's inspect this error:

```console
>>> soup.find_all('h3').text
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/filipacalado/opt/anaconda3/lib/python3.7/site-packages/bs4/element.py", line 2161, in __getattr__
    "ResultSet object has no attribute '%s'. You're probably treating a list of elements like a single element. Did you call find_all() when you meant to call find()?" % key
AttributeError: ResultSet object has no attribute 'text'. You're probably treating a list of elements like a single element. Did you call find_all() when you meant to call find()?
```

We see the line `ResultSet object has no attribute 'text'`, which means that the element we are trying to access cannot return `text`. 

The next line, `You're probably treating a list of elements like a single element. Did you call find_all() when you meant to call find()?` tells us exactly what is wrong. We cannot access the `text` on a list of elements. The pythonic reason is because of the nature of the `find_all()` function returns a list object. In bs4, we cannot get text attributes from a list object. So we have to find another way.

## looping

The solution, in this case, is to create a loop that goes through list of headings. As we loop through each time the list, we take out the desired text.

Before moving forward, let's review briefly Loops for those who are unfamiliar or need refresher.

A `for loop` is two lines of code which *iterates* over a list. That means it goes through each item in the list and does something to it. The first line of code specificies which list, and the second line indicates what to do to each item on the list (the second line needs to be indented with four spaces).

```console
>>> for letter in "hello":
...     print(letter)
... 
h
e
l
l
o
```

This loop goes through each item in the string, and does something. In this case, it prints each letter of the string `hello`.

Let's write a loop to get the text from the `h3` elements. First we make the variable `headers`:

```console
>>> headers = soup.find_all('h3') # create a list of the h3 elements
>>> headers # returns a list of our h3 elements
```

Then we write the loop - for each item in the list, print the text of that item. Remember, we are using dot syntax to acces the text from the header item.

```console
>>> for item in headers:
        print(item.text)
```	 

## scrape_headings.py

Let's make our little script more efficient -- let's create a function that grabs all headings on its own. It will loop through the headings in the webpage and add those headings to the list. 

Open a new file, save it as `scrape_headings.py`, and write the following lines of code: 

```console
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
```

This kind of thing is useful because then we can automate the process of getting text from different elements. 

## practice time!

In breakout groups, write a loop so it prints the paragraphs `<p>` of nyt. Change up the variable names as well, so that they reflect that we are looking for paragraphs and not headings. 

# inspecting pages

Now we are going to learn how to use web browser tools to help us write scripts for scraping websites. Specifically, we are going to look for information we need in order to get data from the links on the New York Times homepage. We want to get data about the links, the text of each link, and the URL for each link. Our goal is to write a script that will grab the link data and URL data from the homepage. 

## inspect element

Open up a web browser, go to the New York Times website. Right click on a headline, any headline, and select `inspect element` (or whatever option is closest to that phrase in your menu).

A new window will pop up within your browser window. This window may appear overwhelming, but it's just a little look 'under the hood' of the website. 

This is the best tool for web scraping, or any kind of web development work, because it allows us to 'inspect' html elements. As I pan over different lines of code, you can see that some areas of the webpage become highlighted. Those are the parts that correspond to the code. 

It's important to reinforce how inscrutible a lot of this code is. I have no idea what's going on in 90 percent of this page, but that doesn't mean I cannot work with it and scrape it. The inspector tool is the best help here, as it allows you to explore the page and see what's going on behind the scenes.

Let's inspect the headline again, paying close attention to what is around it. We notice that on this page, the link tag `a` is actually wrapping around the headline element `h3`. This makes sense, because clicking on any part of the headline (or the area of the headline) will automatically take us to the linked article. 

As we continue to inspect the headline area, another thing we notice is that it's contained by a series of `<divs>`, so many of them, and also by a single `<section>` element, which contains a class, `story-wrapper`. If we look at other headlines, we will that all of the, are contained by this class, `story-wrapper`.

## classes, text, attributes

In our case, we want to scrape the text from these headlines. Using the `story-wrapper` class seems like the best way to go, because it encloses the link text and the link URL. Whenever you are scraping a webpage, you should spend some time looking in the inspector to see what you are looking at.

To scrape the links and the link text, let's first write an expression that prints these elements with the `story-wrapper` class, noticing the new syntax for `class_`:

```console
>>> soup.find(class_ = "story-wrapper")
```

Here we get the first headline, a rather big clunk of text containing links, taglines, other elements, etc. 

Now let's just get the text:

```console
>>> soup.find(class_ = "story-wrapper").text
```

Before doing anything else, let's save the `story-wrapper` data to a variable. That way, we will be able to do things more easily to this data.

```console
>>> story_wrapper = soup.find(class_ = "story-wrapper")
>>> story_wrapper
```

This returns the entire story_wrapper element, the chuck we saw before. Now, we can return just the text by running:

```console
>>> story_wrapper.text
```

This output is cleaner, but what if I wanted to get just the link?

To get just the link info, search the "anchor" element, the `a` element (the link). 

```console
>>> story_wrapper.a
```

Now, to get just the link URL, use syntax for accessing attributes. Again, the syntax is: `tag['attr']`; how we get attributes like hyperlink reference we are accessing it like we access a dictionary in python.

```console
>>> story_wrapper.a['href']
```

Additionally, if we want the text that goes with the link (the part that we see when we click on the link), we can search for just the text in `a`:

```console
>>> story_wrapper.a.text
```

To sum up, so far: we have been using the `story-wraper` class to access data from this webpage. We have been able to get the text that goes with the `story-wrapper` class itself, and the `a` tag (with `a.text`), as well as the specific URL from the `['href']` attribute (with `a['href']`. 

# final activity

Now that we have what we need, we are going to create a little script that loops through NYT data to pull out the headlines and links, and output that data to a spreadsheet (csv file) for further analysis.

## looping through a class

Pulling together everything we've learned so far, we could now write ourselves a loop that grabs all of the links from this page `a['href']`, as well as a loop that gets just the headlines associated with the links `a.text`.

Let's first create a story_wrapper object, which contains a list of all story_wrappers on the page. Then we can write a loop that grabs two things--headline and the link. 

```console

>>> story_wrappers = soup.find_all(class_ = "story-wrapper")

>>> for item in story_wrappers:
        print(item.a.text)
        print(item.a['href']
```

Now we can see in the terminal output a nice little list of all our headlines with the links that are anchored to them.

## print to csv file

All of this scraping is great, but we should also think about way to work with the data we create. In order to do that, we need to save the data to a workable format, like CSV (comma separated values, a spreadsheet).

First, back in the terminal (exiting python environment with the command `exit()`), install the `csv` python library: 

```
% pip install csv
```

Then we create a new script, let's name it `scrape_to_csv.py` which contains the following lines:

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

Notice there are a few new lines here, which have to do with importing and setting up our csv file.
	
After running this file in the terminal, we should see the output in our present working directory. Open the file to check that we have the correct output.

AND THAT'S IT! You have now learned the basic steps of pulling data, organizing it, and saving it with bs4.

The next steps is to analyze that data. For that, you have several choices, such as text analysis with NLTK (natural langauge toolkit), or data analysis with pandas (python data anlaysis & manipulation), which are not covered in this workshop. But we do have resources on these!

# next steps

First, be sure to check out our other workshops by GCDI digital fellows:

[Text Analysis with NLTK workshop](https://curriculum.dhinstitutes.org/workshops/text-analysis/)

[Data Analysis with Pandas workshop](https://digitalfellows.commons.gc.cuny.edu/2021/04/09/exploring-data-with-python-and-pandas/)

Here are some other tutorials from the internet, specifically for web scraping social media. 

[Scraping reddit into JSON format](https://www.scrapehero.com/a-beginners-guide-to-web-scraping-part-2-build-a-scraper-for-reddit/). 
Script (with walkthrough) on how to scrape data from Reddit. 
Although reddit also has a handy ![api](https://www.reddit.com/dev/api/). 

[Instagram-scraper](https://github.com/arc298/instagram-scraper). 
Module for scraping instagram that outputs automatically into JSON file. 

*Quickstart with instagram-scraper*. Read the rest of the user guide to scrape other information, including private accounts.

```console
% pip install instagram-scraper
% instagram-scraper [enter username without brackets]
```

# sources

[Beautiful Soup 4 docs](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

[Beautiful Soup 4 on PiPy](https://pypi.org/project/beautifulsoup4/)

[Corey's Schafer's YouTube tutorial, from html to csv](https://www.youtube.com/watch?v=ng2o98k983k)

[Real Python's web scrapping with bs4 tutorial](https://realpython.com/python-web-scraping-practical-introduction/)
