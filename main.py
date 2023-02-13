import re

print("Kalkulator\n")

# aby zakończyć rozgrywke należy wcisnąć q

wczesniejszy=0

run=True

def wyswietl():
    global run
    global wczesniejszy

    rownanie=input("Wpisz dzialanie: ")
    if rownanie=="q":
        run=False
    else:
        # eliminacja wszystkich innych niewskazanych znaków w kalkulatorze
        rownanie=re.sub("[A-Za-z,.:]","",rownanie)
        if rownanie=="":
            rownanie="0"
        # eval() rozwiązuje podane rówanie 
        wczesniejszy=eval(rownanie)
        print(wczesniejszy)

while run:
    wyswietl()