#Code for openeing random, recent scientific journal article, drawn from Science Daily


    #Step 0: Get proper imports
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
import webbrowser
import random
import requests

    #Step 1: Define function
def random_journal():
    #Step 2: Open up to ScienceDaily and create soup object
    req = Request(
        url='https://www.sciencedaily.com/news/', 
        headers={'User-Agent': 'Mozilla/5.0'})
    html_page = urlopen(req).read()

    soup = BeautifulSoup(html_page, "lxml")

    #Step 3: Get all links
    links = []
    for link in soup.findAll('a'):
        links.append(link.get('href'))

    #Step 4: Get only links to release summaries
    links2 =[]
    for link in links:
        if '.htm' and '/releases' in link:
            links2.append(link)

    #Step 5: Randomoly select release summary
    r_article = random.choice(links2)
    r_page ='https://www.sciencedaily.com' + r_article

    #Step 6: Get all text from release summmary page
    r = requests.get(r_page, headers = {'User-Agent': 'Mozilla/5.0'})
    r.text

    #Step 7: Get reference to original article and open in new browser tab
    start=r.text.find("Journal Reference")
    end=r.text.find("Cite This Page")
    coverage=r.text[start:end]
    coverage2 = coverage.split(' ')
    for item in coverage2:
        if 'href' in item:
            return webbrowser.open_new(item.strip("href="))

