
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

# Create your views here.


#ABC NEWS
abc_r = requests.get("https://abcnews.go.com/US/")
abc_soup = BeautifulSoup(abc_r.content, 'html5lib')
abc_headings = abc_soup.findAll('a')
abc_headings = abc_headings[0:]
indices_to_access = [8,9,11,12,13,15,17,18,19,20,22,26,28,30,34,36,40,42,44,46,48,50,52,54,
56,58,60,62,64,66,68,72,76,78,80,82,86,90,92,94,96,98,100,102,104,106,108,110]
accessed_mapping = map(abc_headings.__getitem__, indices_to_access)
abc_headings = list(accessed_mapping)

abc_news = []
  
for abch in abc_headings:
    abc_news.append(abch.text)
 

#ABC NEWS2
abc2_r = requests.get("https://abcnews.go.com/US/")
abc2_soup = BeautifulSoup(abc2_r.content, 'html5lib')
abc2_headings = abc2_soup.findAll('h3')
abc2_headings = abc2_headings[1:20]

abc_news2 = []

for abc2h in abc2_headings:
    abc_news2.append(abc2h.text)

 

#CBS NEWS
cbs_r = requests.get("https://www.cbsnews.com/us/")
cbs_soup = BeautifulSoup(cbs_r.content, 'html5lib')
cbs_headings = cbs_soup.findAll('h4')
cbs_headings = cbs_headings[0:]
indices_to_access = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,24,26,28,29,32,33,35,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,
56,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,79,81,82,83,84,85]
accessed_mapping = map(cbs_headings.__getitem__, indices_to_access)
cbs_headings = list(accessed_mapping)

cbs_news = []

for cbsh in cbs_headings:
    cbs_news.append(cbsh.text)



def index3(req):

    return render(req, 'news/index3.html', {'abc_news':abc_news, 'abc_news2':abc_news2, 'cbs_news':cbs_news})


  
      