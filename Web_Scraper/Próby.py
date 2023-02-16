import simplejson as json
#do info dotyczących plików
import os

#czy istnieje taki plik i czy nie jest pusty
if os.path.isfile("./ages.json") and os.stat("./ages.json").st_size!=0:
    old_file=open("./ages.json","r+")
    #aby móc przeczytać do python useble obj
    data=json.loads(old_file.read())

    print("Wiek wynosi: ",data["age"])
    #zwiększenie roku
    data["age"]=data["age"]+1
    print("Teraz nowy wiek wynosi: ",data["age"])

else:
    old_file=open("./ages.json","w+")
    data={"name": "Martyna","age": 22}
    print("Nie znalazałem pliku, ale go stworzyłem")

#na początek
old_file.seek(0)
#zapis do formatu json
old_file.write(json.dumps(data))