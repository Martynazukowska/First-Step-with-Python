from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO

search=input("Co mam wyszukać: ")

dodatkowy={"q":search}
r=requests.get("https://www.bing.com/images/search",params=dodatkowy)

#soup to cała strona
soup=BeautifulSoup(r.text, "html.parser")

#wiem co ze strony ktora przeszukuje
links=soup.findAll("a", {"class": "thunb"})


#wypisz strone i jej url
for item in links:
    ing_obj=requests.get(item.attrs["href"])
    #tytuł z internetu
    title=item.attrs["href"].split("/")[-1]
    img=Image.open(BytesIO(ing_obj.content))
    img.save("./"+title,ing.format)    