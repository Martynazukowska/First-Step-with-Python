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

    def get_zycie(self):
        return self.zycie

    def get_zycie_max(self):
        return self.zycie_max

    def get_moc(self):
        return self.moc
    
    def get_moc_max(self):
        return self.moc_max

    def get_zaklecie(self,ktory):
        return self.magic[ktory]

    def losuj_obrazenie(self):
        return random.randrange(self.atakD,self.atakG)
    
    def take_obrazenie(self,obrazenie):
        self.zycie-=obrazenie
        if self.zycie<0:
            self.zycie=0

    def odswiez_moc(self,koszt):
        self.moc-=koszt

    def choose_action(self):
        i=1
        for item in self.action:
            print(str(i)," : ",item)
            i+=1
    
    def choose_magic(self):
        i=1
        for item in self.magic:
            print(str(i)," : Nazwa - ", item.get_nazwe_zaklecia(),"       Koszt - ",item.get_koszt_zaklecia())
            i+=1
    