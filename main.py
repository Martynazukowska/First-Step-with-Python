

print("Martyna")
print(int("5")+3)


print("Moje opcje to: "+ "A:B:C".split(":")[0])

#słownik, nie lista odwolujemy się do kategorii a nie do 0/1/2
slownik={"name": "Martyna", "age": 23, "hobby": "jedzenie"}

print(slownik["name"])
print(len(slownik["name"]))

kolejka=[3,55,67,22,34,5,21,4,67,99]

print(sorted(kolejka))

def moja_funkcja():
    print("Funkcja")

moja_funkcja()