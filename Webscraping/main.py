import urllib
import urllib.request
from bs4 import BeautifulSoup

url="http://souranil.de/list-common-birds-part-1/"
page=urllib.request.urlopen(url)
soup=BeautifulSoup(page,"html.parser")

file="result.txt"
f=open(file,"w")
heads = soup.findAll('h3')

for i in range(0,len(heads)-1):
    headfin=str(heads[i].contents[0])
    headfin=headfin.replace("<strong>","",1)
    headfin=headfin.replace("</strong>","",1)
    headfin=headfin.replace(":","",1)
    f.write(str(headfin)+"\n")
    
f.close()

file="input.txt"
f=open(file,"w")
f.write(str(soup.prettify()))
f.close()

for img in soup.findAll('img'):
    image=img.get('src')
    filename=img.get('alt')
    imagefile=open(filename + ".jpeg",'wb')
    imagefile.write(urllib.request.urlopen(image).read())
    imagefile.close()