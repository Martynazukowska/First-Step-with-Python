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


def wypisz(wrog,player1):

    bar=bar_zycie(wrog)
    bar=str(bar)
    bar=re.sub("', ","",bar)
    bar=re.sub("'","",bar)
    print("------------------------------------------------")
    print("      ŻYCIE                                              MOC")
    print("                  ____________________________")
    print("Wrog: "+bcolors.FAIL+str(wrog.get_zycie())+bcolors.ENDC+" / "+bcolors.FAIL+str(wrog.get_zycie_max())+bcolors.ENDC+ 
          " |"+bcolors.FAIL+bar+bcolors.ENDC+"|")

    bar=bar_zycie(player1)
    bar=str(bar)
    bar=re.sub("', ","",bar)
    bar=re.sub("'","",bar)

    bar2=bar_moc(player1)
    bar2=str(bar2)
    bar2=re.sub("', ","",bar2)
    bar2=re.sub("'","",bar2)
    print("                  ____________________________                   _____________")
    print("Ty:   "+bcolors.OKGREEN+str(player1.get_zycie())+bcolors.ENDC+" / "+bcolors.OKGREEN+str(player1.get_zycie_max())+bcolors.ENDC+ 
          "  |"+bcolors.OKGREEN+bar+bcolors.ENDC+"|         "+bcolors.OKBLUE+str(player1.get_moc())+bcolors.ENDC+" / "+
          bcolors.OKBLUE+str(player1.get_moc_max())+bcolors.ENDC+" |"+bcolors.OKBLUE+bar2+bcolors.ENDC+"|")