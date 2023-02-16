import requests

Szukane={"search?q":"pizza"}

r=requests.get("https://www.google.com/",params=Szukane)

print("Status: ",r.status_code)

print(r.url)
#HTML
#print(r.text)

file_html=open("./page.html","w+")

#polecenie poprawne, ale problemy z google i łąduje pustą strone ( na bingu działa)
file_html.write(r.text)