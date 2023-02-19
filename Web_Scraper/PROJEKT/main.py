from bs4 import BeautifulSoup
import requests


search=input("Co mam wyszukać: ")

dodatkowy={"q":search}
r=requests.get("https://www.bing.com/search",params=dodatkowy)

#soup to cała strona
soup=BeautifulSoup(r.text, "html.parser")
#print(soup.prettify())

#wiem co ze strony ktora przeszukuje
to_co_dostales=soup.find("ol",{"id": "b_results"})
links=to_co_dostales.findAll("li",{"class": "b_algo"})

#wypisz strone i jej url
for item in links:
    item_text=item.find("a").text
    # w [] wpisujemy jakiego atrybutu poszukujemy
    item_href=item.find("a").attrs["href"]

    if item_text and item_href:
        print(item_text)
        print(item_href)