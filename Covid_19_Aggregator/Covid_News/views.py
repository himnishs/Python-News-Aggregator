from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

# Create your views here.

#Getting Covid-news from CBS
cbs_r = requests.get("https://www.cbsnews.com/feature/coronavirus/")
cbs_soup = BeautifulSoup(cbs_r.content, 'html5lib')
cbs_newsDivs = cbs_soup.findAll("h4", {"class": "item__hed"})
count_cbs = 0
cbs_news = []
for n in cbs_newsDivs:
    if(count_cbs < 25):
        cbs_news.append(n.text)
    count_cbs += 1


#Getting Covid-News from Fox
fox_r = requests.get("https://www.foxnews.com/category/health/infectious-disease/coronavirus")
fox_soup = BeautifulSoup(fox_r.content, 'html5lib')
fox_newsDivs = fox_soup.findAll("h4", {"class": "title"})
count_fox = 0
fox_news = []
for n in fox_newsDivs:
    if(count_fox < 25):
        fox_news.append(n.text)
    count_fox += 1

#Getting Covid-News from NBC
nbc_r = requests.get("https://www.nbcnews.com/health/coronavirus")
nbc_soup = BeautifulSoup(nbc_r.content, 'html5lib')
newsDivs_nbc = nbc_soup.select("a.vilynx_disabled")
count_nbc = 0
nbc_news = []

for n in newsDivs_nbc:
    if "tease-card__picture-link" in n["class"]:
        continue
    if "pancake__tease-picture-link" in n["class"]:
       continue
    if(n.text == "Coronavirus"):
        continue
    if(n.text == "Opinion"):
        continue
    if(n.text == "Data Graphics"):
        continue
    if(n.text == "WATCH"):
        continue
    if(n.text == ""):
        continue
    if(count_nbc < 25):
        nbc_news.append(n.text)
    count_nbc += 1
 


def index(req):
    return render(req, 'new/index.html', {"cbs_news": cbs_news, "fox_news":fox_news})

