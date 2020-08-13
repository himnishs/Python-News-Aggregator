from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

# Create your views here.

#Getting Covid-news from CBS
cbs_r = requests.get("https://www.cbsnews.com/feature/coronavirus/")
cbs_soup = BeautifulSoup(cbs_r.content, 'html5lib')
cbs_newsDivs = cbs_soup.findAll("h4", {"class": "item__hed"})
cbs_news = []
for n in cbs_newsDivs[:10]:
    cbs_news.append(n.text)

#Getting Covid-News from Fox
fox_r = requests.get("https://www.foxnews.com/category/health/infectious-disease/coronavirus")
fox_soup = BeautifulSoup(fox_r.content, 'html5lib')
fox_newsDivs = fox_soup.findAll("h4", {"class": "title"})
fox_news = []
for n in fox_newsDivs[1:11]:
    fox_news.append(n.text)

#Getting Covid-News from NBC
nbc_r = requests.get("https://www.nbcnews.com/health/coronavirus")
nbc_soup = BeautifulSoup(nbc_r.content, 'html5lib')
newsDivs_nbc = nbc_soup.select("a.vilynx_disabled")
count_nbc = 0
nbc_news = []

for n in newsDivs_nbc[2:20]:
    if "tease-card__picture-link" in n["class"]:
        continue
    if "pancake__tease-picture-link" in n["class"]:
       continue
    if(n.text == "Coronavirus" or n.text == "coronavirus"):
        continue
    if(n.text == "Opinion"):
        continue
    if(n.text == "Data Graphics"):
        continue
    if(n.text == "WATCH"):
        continue
    if(n.text == ""):
        continue
    nbc_news.append(n.text)
 
def index(req):
    return render(req, 'Covid_News/index.html', {"cbs_news": cbs_news, "fox_news":fox_news, "nbc_news": nbc_news})

