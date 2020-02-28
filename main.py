from bs4 import BeautifulSoup
import requests

r = requests.get("https://news.google.com/?hl=nl&gl=NL&ceid=NL:nl")
if r.status_code == 200:
    print("Link is correct")
else:
    print("unvalid link")

soup = BeautifulSoup(r.text, 'html.parser')
inf = soup.find_all("h3", href=False)
print(type(inf))
store = []
for i in inf:
    store.append(i)

with open('store.html', 'w') as filehandle:
    for listitem in store:
        filehandle.write('%s\n' % listitem)

with open("store.html", "r") as f:
    contents = f.read()

soup = BeautifulSoup(contents, 'html.parser')
headline = soup.get_text()

with open('store.txt', 'w') as filehandle:
    for listitem in headline:
        filehandle.write('%s' % listitem)





