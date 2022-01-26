import pandas as pd
import urllib.request
from bs4 import BeautifulSoup


urllib.request.urlretrieve("http://127.0.0.1:8000/text/", "input.txt")
file = open("input.txt", "r")
contents = file.read()
soup = BeautifulSoup(contents, 'html.parser')
f = open("output.txt", "w")


for data in soup.find_all("li"):
    sum = data.get_text()
    f.writelines(sum + '\n')

f.close()
