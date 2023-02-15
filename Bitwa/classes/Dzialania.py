from .game import bcolors
import re

def bar_zycie(osoba):
    hp=" "
    i=0
    hp_cale=[]
    while i<=25:
        hp_cale.append(hp)
        i+=1

    x=osoba.get_zycie()/osoba.get_zycie_max()*25
    i=0
    while i<=x:
        hp_cale[i]="X"
        i+=1
    return hp_cale


def bar_moc(osoba):
    hp=" "
    i=0
    hp_cale=[]
    while i<=10:
        hp_cale.append(hp)
        i+=1

    x=osoba.get_moc()/osoba.get_moc_max()*10
    i=0
    while i<=x:
        hp_cale[i]="X"
        i+=1
    return hp_cale

#Funkcja potrzebna aby bar się nie przesówał
def liczba_zycia(osoba):
    pom_zycie=str(osoba.get_zycie())
    pom_zycie_max=str(osoba.get_zycie_max())
    if len(pom_zycie)-len(pom_zycie_max)<0:
        pom=len(pom_zycie_max)-len(pom_zycie)
        while pom > 0:
            pom_zycie+=" "
            pom-=1
    return pom_zycie


#Funkcja potrzebna aby bar się nie przesówał
def liczba_mocy(osoba):
    pom_mocy=str(osoba.get_moc())
    pom_moc_max=str(osoba.get_moc_max())
    if len(pom_mocy)-len(pom_moc_max)<0:
        pom=len(pom_moc_max)-len(pom_mocy)
        while pom > 0:
            pom_mocy+=" "
            pom-=1
    return pom_mocy


def wypisz(wrog,player1):
    #zycie wroga - bar
    bar=bar_zycie(wrog)
    bar=str(bar)
    bar=re.sub("', ","",bar)
    bar=re.sub("'","",bar)
    print("------------------------------------------------")
    print("      ŻYCIE                                              MOC")
    print("                   ____________________________")
    print("Wrog: "+bcolors.FAIL+liczba_zycia(wrog)+bcolors.ENDC+" / "+bcolors.FAIL+str(wrog.get_zycie_max())+bcolors.ENDC+ 
          " |"+bcolors.FAIL+bar+bcolors.ENDC+"|")

    #nasze zycie - bar 
    bar=bar_zycie(player1)
    bar=str(bar)
    bar=re.sub("', ","",bar)
    bar=re.sub("'","",bar)
    #nasza moc - bar
    bar2=bar_moc(player1)
    bar2=str(bar2)
    bar2=re.sub("', ","",bar2)
    bar2=re.sub("'","",bar2)
    print("                  ____________________________                   _____________")
    print("Ty:   "+bcolors.OKGREEN+liczba_zycia(player1)+bcolors.ENDC+" / "+bcolors.OKGREEN+str(player1.get_zycie_max())+bcolors.ENDC+ 
          "  |"+bcolors.OKGREEN+bar+bcolors.ENDC+"|         "+bcolors.OKBLUE+liczba_mocy(player1)+bcolors.ENDC+" / "+
          bcolors.OKBLUE+str(player1.get_moc_max())+bcolors.ENDC+" |"+bcolors.OKBLUE+bar2+bcolors.ENDC+"|")