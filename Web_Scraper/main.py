import requests
from io import BytesIO
from PIL import Image

#świnka
r=requests.get("https://www.zooplus.pl/magazyn/wp-content/uploads/2021/05/mikroswinka-768x513.jpeg")

print("status:",r.status_code)

image=Image.open(BytesIO(r.content))

sciezka="./image."+image.format

#info o śwince
print(image.size,image.format,image.mode)

#zapisz obrazek
try:
    image.save(sciezka,image.format)
except IOError:
    print("Coś poszło nie tak przy zapisie")