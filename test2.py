import re
import requests
from bs4 import BeautifulSoup

string = "one ok rock"

url = "https://www.youtube.com/results?search_query=" + string
res = requests.get(url, verify=False)
soup = BeautifulSoup(res.text,'html.parser')

for entry in soup.select('a'):
    m = re.search("v=(.*)", entry['href'])
    if m:
        print m.group(1)

