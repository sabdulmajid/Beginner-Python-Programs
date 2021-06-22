import requests
from bs4 import BeautifulSoup

user_input = input('Enter the word you seek: \n')
web = requests.get('https://www.lexico.com/definition/' + user_input)

data = web.content

soup = BeautifulSoup(data, features = "html.parser")

a = 1
tag = soup.find_all("span", "ind")

for i in tag:
    print(a, '.',i.text)
    a = a + 1
