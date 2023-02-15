from .game import bcolors


def wypisz(wrog,player1):
    print("------------------------------------------------")
    print("      ŻYCIE                                              MOC")
    print("                  _________________________")
    print("Wrog: "+bcolors.FAIL+str(wrog.get_zycie())+bcolors.ENDC+" / "+bcolors.FAIL+str(wrog.get_zycie_max())+bcolors.ENDC+ 
          " |"+bcolors.FAIL+"XXXXXXXXXX               "+bcolors.ENDC+"|")
    print("                  _________________________                      __________")
    print("Ty:   "+bcolors.OKGREEN+str(player1.get_zycie())+bcolors.ENDC+" / "+bcolors.OKGREEN+str(player1.get_zycie_max())+bcolors.ENDC+ 
          "  |"+bcolors.OKGREEN+"XXXXXXXXXX               "+bcolors.ENDC+"|            "+bcolors.OKBLUE+str(player1.get_moc())+bcolors.ENDC+" / "+
          bcolors.OKBLUE+str(player1.get_moc_max())+bcolors.ENDC+" |"+bcolors.OKBLUE+"XXX       "+bcolors.ENDC+"|")