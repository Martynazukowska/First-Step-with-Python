import re

print("Kalkulator\n")

# aby zakończyć rozgrywke należy wcisnąć q

wczesniejszy=0
start=0
#zmienna potrzebna do logicznego zapisu
prewczesniejszy=0

run=True

def wyswietl():
    global run
    global wczesniejszy
    global start
    global prewczesniejszy

    #jeśli zaczynamy działanie
    if start==0:
        rownanie=input("Wpisz dzialanie: ")
    #jeśli rozpisujemy wcześniejsze działanie
    else:
        rownanie=input(str(wczesniejszy))

    #jeśli koniec ...
    if rownanie=="q":
        run=False
    #jeśli nie koniec
    else:
        # eliminacja wszystkich innych niewskazanych znaków w kalkulatorze
        rownanie=re.sub("[A-Za-z,.:]","",rownanie)
        if rownanie=="":
            rownanie="0"

        if start==0:
            prewczesniejszy=""
            # eval() rozwiązuje podane rówanie 
            wczesniejszy=eval(rownanie)
            start=start+1
        else:
            prewczesniejszy=wczesniejszy
            wczesniejszy=eval(str(wczesniejszy)+rownanie)
        
        #wyświetlanie całego równania na kalkulatorze
        print(prewczesniejszy,rownanie,"=",wczesniejszy)


while run:
    wyswietl()