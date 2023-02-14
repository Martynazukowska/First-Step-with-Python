import random


class bcolors:
    HEADER    = '\033[95m'
    OKBLUE    = '\033[94m'
    OKGREEN   = '\033[92m'
    WARNING   = '\033[93m'
    FAIL      = '\033[91m'
    BOLD      = '\033[1m'
    UNDERLINE = '\033[4m'
    ENDC      = '\033[0m'

class Osoba:
    def __init__(self,zycie,moc,atak,obrona,magic):
        self.zycie=zycie
        self.moc=moc
        self.zycie_max=zycie
        self.moc_max=moc
        self.atakG=atak+10
        self.atakD=atak-10
        self.obrona=obrona
        self.magic=magic

        self.action=["Atak","Magic"]

    def losuj_obrazenie(self):
        return random.randrange(self.atakD,self.atakG)
    
    def losuj_magic(self,ideks_zaklecia):
        zaklecie_zakresD=self.magic[ideks_zaklecia]["obrazenia"]-10
        zaklecie_zakresG=self.magic[ideks_zaklecia]["obrazenia"]+10
        return random.randrange(zaklecie_zakresD,zaklecie_zakresG)

    