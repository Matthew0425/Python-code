from bs4 import BeautifulSoup
import requests

valid_links = {}

math_notes_link = "http://tutorial.math.lamar.edu/Classes/DE/DE.aspx"
math_notes_link_2 = "http://tutorial.math.lamar.edu/Classes/DE"

r = requests.get(math_notes_link)

soup = BeautifulSoup(r.content, features='lxml')

for item in soup.find_all("a", {'class': 'introlink'}):
    valid_links[item.text] = item.get('href')

print("Valid Links:")
for item in valid_links:
    #print(item, ": ", valid_links[item])
    print(item)

where = input("Please input a known section of this website >>")

ticket = False
while not ticket:
    for item in valid_links:
        if item == where:
            ticket = True
    if not ticket:
        print("Invalid link, try again")
        where = input("Please input a known section of this website >>")

math_notes_link_2 += "/" +  valid_links[where]

print(math_notes_link_2)

r = requests.get(math_notes_link_2)

soup = BeautifulSoup(r.content, features='lxml')

for item in soup.find_all('p'):
    print(item.text)
