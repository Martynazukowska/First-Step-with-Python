import random


print("Moje opcje to: "+ "A:B:C".split(":")[0])

#słownik, nie lista odwolujemy się do kategorii a nie do 0/1/2
slownik={"name": "Martyna", "age": 23, "hobby": "jedzenie"}

print(slownik["name"])
print(len(slownik["name"]))

kolejka=[3,55,67,22,34,5,21,4,67,99]

#sortowanie int lub string obojentne 
print(sorted(kolejka))

#tworzenie funkcji
def moja_funkcja(pierwszy,drugi):
    print(pierwszy,2+drugi)


moja_funkcja("Funkcja", -1)
moja_funkcja("Teraz funkcja", 0)

zmienna=[1,2,3,4]

#wszystkie wartości wchodzące do funkcji
def spis_ludzi(*czlowiek):
    for ktos in czlowiek:
        print("Ten ktos to: ", ktos)


class Enemy:
#    atakD=0
#    atakG=0
    def __init__(self,D,G):
        self.atakD=D
        self.atakG=G

    def getAtakD(self):
        return self.atakD
    def getAtakG(self):
        return self.atakG


def losuj():
    Atak=Enemy(60,80)
    zycia=250
    atakDol=Atak.getAtakD()
    atakGora=Atak.getAtakG()

    while zycia>0:
        #losuj z zakresu odpowiedni atak
        atak=random.randrange(atakDol,atakGora)
        zycia=zycia-atak
        if zycia>0:
            print("Atak wynosi ",atak," po nim twoje życie wynosi ", zycia)
            continue
        
        print("Atak wynosi ",atak," po nim twoje życie wynosi ", zycia)
        print("Game over")
        break



# Sprawdzanie działania napisanych funkcji
for item in zmienna:
    if item==1:
        #tworzenie default wartości funkcji
        def moja_funkcja2(pierwszy="Uwaga błąd",drugi=-10001):
            print(pierwszy,2+drugi)

        moja_funkcja2("Funkcja", -1)
        moja_funkcja2()

    elif item==2:
        #inne wywoływanie funkcji 
        moja_funkcja2(drugi=0,pierwszy="Zamiana miejsca")

    elif item==3:
        print("\n")
        spis_ludzi("Ola", "Kuba", "Zuza")

    else:
        print("\n")
        spis_ludzi("Ola", "Zuza")
        print("\n")
        losuj()

