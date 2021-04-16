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

I will be sharing my screen, demonstrating how to do things. You might follow along by watching, or typing as I type, if this topic is very new or confusing, just watch for now. Occasionally, there will be time for practice, where I give you time to replicate what I am doing.

And do not worry about falling behind, all of the code that I type is saved to a ![separate file](relativepath), so you're not going to miss anything

Rafa and Steve are here to help out. Rafa on the chat to answer questions, Steve mostly for aesthetics. Feel free to interrupt as well!

At the beginning e will cover some basics on HTML and Command Line. Apologies to those more advanced users, but it's necessary to get the most engagement for the group.

## what is web scraping

Web scraping is pulling or extracting data from webpages, their HTML files. 

### Web scraping vs requesting data from APIs
- API - application programming interface, allowing you to talk to an app, request data
- both are about getting data from websites, resources
- except, APIs are created by the data holders, more efficient, with ready JSON, XML
- for example, social media,  weather, sports, financial data, libraries & archives
- Web Scraping is when you pull data directly from the website. Then you convert it
- Web Scraping is more work, more coding, with less support from the source

### Some considerations:

If there is an API that returns JSON, XML, use that before scraping. 

You might find yourself in a scenario where there might not be an API to access the data you want, or the access to the API might be too limited  or expensive. 

There are potential legal issues with web scraping if a website doesn't allow it.

## required software

Install python and pip 

Click here to install our recommended python distribution, ![Anaconda](https://www.anaconda.com/products/individual). Scroll to the bottom of the page, and click the relevant version for your machine.

Click here to ![install pip](https://pip.pypa.io/en/stable/reference/pip_install/) (python package manager, ie allows you to install python libraries like bs4). 

This part might take a few minutes, so be patient. 
 
Once you have python & pip, let's check you have the rest of the python packages: requests (for requesting data over the web), bs4 (the beautiful soup 4 package), and lxml (the recommended parser for bs4).

```console
% pip install requests
% pip install bs4
% pip install lxml
```
 
## quick intros to HTML & Command Line

This workshop assumes basic familiarity with python, HTML, and the command line. In the case that you do *not* have this knowledge, I highly recommend reading through these GC Digital Humanities Research Institute materials:

- DHRI workshop on ![the Command Line](https://curriculum.dhinstitutes.org/workshops/command-line/) (complete lessons 1-6, through "Navigation")
- DHRI workshop on ![HTML/CSS](https://curriculum.dhinstitutes.org/workshops/html-css/) (complete lessons 1-6, through "Links")
- DHRI workshop on ![Python](https://curriculum.dhinstitutes.org/workshops/python/) (complete lessons 1-7, through "Loops")

Just as a refresher, I'm going to  sample HTML file. We will be paying attention to **head** elements, including the **title**, **h1**, **h2** tags, and the **body** elements, including **a** and **p** tags, as well as some attributes like **class** and **href**. 

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

Now to the Command Line. On your computer, the Command Line might be Terminal (if you have a Mac) or Powershell or Gitbash (if you have Windows). 

Once you've opened your command line program, type `pwd` to check what directory you are inside (in other words, where you are on your computer). You're likely in the home folder. Go ahead and navigate to your Desktop or Documents folder (wherever you like to work on new projects). For me, I have to type `cd Desktop` to get to my desktop folder. 

Once we are in our desired directory, we can enter the Python interactive mode (ie, the Python shell, or Python interpreter, as it's also known). We enter this mode by typing "python" at the `%` (or `$`, depending on your computer) prompt. 

```console
% python
```

Once we get a result like below, we know we are in the interactive mode.

```console
% python
Python 3.7.7 (default, May  6 2020, 04:59:01) 
[Clang 4.0.1 (tags/RELEASE_401/final)] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

If this is confusing for you, make sure you check out the Command Line tutorial above.

# quick start into bs4

Now we have an interactive shell, let's see jump into bs4 to see what we can do. First, we will import the package, then we will create a beautiful soup object. Inside that object, we will include some HTML.

```console
>>> from bs4 import BeautifulSoup
>>> soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
```
Our bs4 object takes the source HTML and converts it into something that we can work with.

Now we can print the soup, using the `prettify()` function to make it easier to read. 

```console
>>> print(soup.prettify())
```

Here we see the basic HTML structure, with head, bold, paragraph tags. Beautiful soup creates this `soup` object which parses the HTML data into this tree structure.

In concise terms, we've created a beautiful soup object `soup` which contains attributes (or information) like `p` for paragraph, `b` for bold, and `body` for body. 

Let's take an initial look into what this beautiful soup object can do. It takes the HTML source, the specific HTML elelements or "tags," and makes it possible for us to access those tags using python syntax. 

```console
>>> soup.p # prints paragraph
>>> soup.b # prints bolded text
>>> soup.body # prints entire body element
```

Using python syntax to access HTML elements is beautiful soup in a nutshell. 
 
## how to scrape in 7 lines of code

One of the more impressive things about beautiful soup is how much it can do with just a few lines of code. We can scrape an entire webpage, for example. 

I'll show you how it's done with the ![New York Times](https://www.nytimes.com/) website.

First, activate your python shell. Then import your packages. Afterward, we have three lines of code that grab and save website data, and create a beautiful soup object which we can query.  

```console
>>> import requests
>>> from bs4 import BeautifulSoup

>>> webpage = requests.get("https://www.nytimes.com")
>>> source = webpage.content
>>> soup = BeautifulSoup(source, 'lxml')
```

For the `webpage` variable, we use the `get()` function from requests to access the webpage. The webpage is the parameter here (the thing in parenthesis). 

Then, we save all page content to source variable in the `source` variable.

Finally, we pass `source` to the `BeautifulSoup` class, alson with `'lxml'`, to create the soup object.

We can print the entire thing (the `soup` object) in our terminal with one more line of code, which includes the `prettify()` function.

```console
>>> soup.prettify()
```

This is pretty overwhelming, because it's the entire source HTML for the front page of the New York Times. But there are other ways we can access the elements with specificity. 

We can get the webpage title:
```console
>>> soup.find('title')
```

We can also search just the readable text, getting rid of all the html tags. 
```console
>>> soup.get_text()
```

# practice time! 

Now you try replicating this process in your terminal. Write your own script for a website, using any URL you want.

Practice accessing attributes like `title` and using functions like `get_text()` and `prettify()`.

# bs4 components

As you are starting to see, beautiful soup comes with a set of custom python functions for searching HTML. It can search HTML tags like `<p>` and attributes like `href`. We can use it look for things in varying amounts of specificity. We can even write our own functions to look for things.

## find()

We might look for a paragraph:

```console
>>> soup.find('p')
```

Here, we look at the soup object (our content), run the "find" function, specifying the "p" as param.

We can also do the same thing while saving our data to a variable.

```console
>>> paragraph = soup.find('p')
>>> print(paragraph)
```

Saving to a variable is useful for doing more complex things (you'll see!).

Let's look for titles, also saving to variable:

```console
>>> title = soup.find('title')
>>> print(title)
```

Note that the output prints the title variable, containing the whole element, with text.

Now, let's look for a link:

```console
>>> link = soup.find('a')
>>> print(link)
```

There's another way of accessing HTML elements, without using the `find()` function. Instead, we just use the dot syntax in python.

```console
% soup.a # print first link
% link = soup.a
```

What other elements can we access?

```console
>>> soup.h1
>>> soup.h2
>>> soup.h3
```

## text & attributes

Let's go a little deeper than the element. We can access just the text (getting rid of tags) from elements.

```console
>>> soup.p.text
```

Here we see just the text, so everything that being wrapped by HTML elements.

We can do it with links too:

```console
>>> link_text = soup.a.text
>>> print(link_text)
```

In addition to text, we can also get the attributes:

```console
>>> soup.a['href']
```

Here, the syntax uses square brackets and single quotes to get `href`, which is the same syntax that we use to get values from python dictionaries. 

Let's save the 

```consle
>>> link_location = soup.a['href']
>>> print(link_location)
```

## find_all()

Want to print out all of a certain element? Then we use `find_all()`

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

But how do we get a list of the headers? You think `soup.find_all('h3').text` would work, would be the correct syntax, but it gets an error. Let's inspect this error:

```console
>>> soup.find_all('h3').text
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/filipacalado/opt/anaconda3/lib/python3.7/site-packages/bs4/element.py", line 2161, in __getattr__
    "ResultSet object has no attribute '%s'. You're probably treating a list of elements like a single element. Did you call find_all() when you meant to call find()?" % key
AttributeError: ResultSet object has no attribute 'text'. You're probably treating a list of elements like a single element. Did you call find_all() when you meant to call find()?
```

We see the line `ResultSet object has no attribute 'text'`, which means that the element we are trying to access cannot return `text`. 

The next line, `You're probably treating a list of elements like a single element. Did you call find_all() when you meant to call find()?` tells us exactly what is wrong. We cannot access the `text` on a list of elements. So we have to find another way.

## looping

The solution, in this case, is to create a list of headings. Then, we can loop through the list, and take out the desired text.

Before moving forward, let's review briefly Loops for those who are unfamiliar or need refresher.

A `for loop` is two lines of code which *iterates* over a list. That means it goes through each item in the list and does something to it. 

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

Let's write a loop to get the text from the `h3` elements. 

```console
>>> headers = soup.find_all('h3') # create a list of the h3 elements
>>> headers # returns a list of our h3 elements
```

Here is the loop - for each item in the list, print the text of that item. Remember, we are using dot syntax to acces the text from the header item.

```console
>>> for item in headers:
        print(item.text)
```	 

## scrape_headings.py

Let's make our little script more efficient -- let's create a function that grabs all headings on its own. It will loops through the headings in the webpage and add those headings to a list. 

This kind of thing is useful because then we can automate the process of getting text from different elements. 

```console
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
```

# practice time!

In breakout groups, write a loop so it prints the paragraphs `<p>` of nyt. Change up the variable names as well, so that they reflect that we are looking for paragraphs and not headings. 

# inspecting pages to access classes

Now we are going to learn how to use web browser tools to help us write scripts for scraping websites.

Open up a web browser, go to the New York Times website. Right click on a headline, any headline, and select `inspect element` (or whatever option is closest to that phrase in your menu).

A new window will pop up within your browser window. This window may appear overwhelming, but it's just a little look 'under the hood' of the website. This is the best tool for scraping, because it allows us to 'inspect' html elements. 

As I pan over different lines of code, you can see that some areas of the webpage are highlighted. Those are the parts that correspond to the code. 

Whenever you are scraping a webpage, you should spend some time looking in the inspector to see what you aare looking at. Looking at these elements, we see that all of the headlines and text blurbs are contained by a class, `story-wrapper`.

Let's print these, noticing the syntax for "class_"

```console
>>> soup.find(class_ = "story-wrapper")
```

Here we get the first headline, a rather big clunk of text containing links, taglines, other elements, etc. 

Now let's just get the text:

```console
>>> soup.find(class_ = "story-wrapper").text
```

Cleaner, but what if I wanted to get just the link?

First, create a variable:

```console
>>> story_wrapper = soup.find(class_ = "story-wrapper")
>>> story_wrapper
```
This returns the entire story_wrapper element, the chuck we saw before.

Second, to get just the link info, search the "anchor" element, the `a` element (the link). 

```console
>>> story_wrapper.a
```

Third, to get just the link, use syntax for accessing attributes:

```console
>>> story_wrapper.a['href']
```

Again, the syntax is: `tag['attr']`; how we get attributes like hyperlink reference we are accessing it like we access a dictionary in python.

Finally, search for just the text in `a`:

```console
>>> story_wrapper.a.text
```

## creating a list to loop through elements by classs

Pulling togethe everything we've learned so far, we could now write ourselves a loop that grabs all of the links from this page, as well as a loop that gets just the headlines associated with the links.

Let's first create a story_wrapper object, which contains a list of all story_wrappers on the page. Then we can write a loop that grabs two things--headline and the link. 

```console

>>> story_wrappers = soup.find_all(class_ = "story-wrapper")

>>> for item in story_wrappers:
		print(item.a.text)
        print(item.a['href']
```

# print to csv file

All of this scraping is great, but we should also think about way to work with the data we create. In order to do that, we need to save the data to a workable format, like CSV (comma separated values, a spreadsheet).

First, back in the terminal (exiting python environment), install csv:

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
	
After running this file in the terminal, we should see the output in our present working directory. Open the file to check that we have the correct output.

AND THAT'S IT!

You have now learned the basic steps of pulling data, organizing it, and saving it. 

The next steps is to analyze that data. For that, you have several choices, such as text analysis with NLTK (natural langauge toolkit), or data analysis with pandas (python data anlaysis & manipulation), which are not covered in this workshop. But we do have resources on these!

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