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

    def losuj_obrazenie(self):
        return random.randrange(self.atakD,self.atakG)
    
    def losuj_magic(self,ideks_zaklecia):
        zaklecie_zakresD=self.magic[ideks_zaklecia]["obrazenia"]-10
        zaklecie_zakresG=self.magic[ideks_zaklecia]["obrazenia"]+10
        return random.randrange(zaklecie_zakresD,zaklecie_zakresG)
    
    def take_obrazenie(self,obrazenie):
        self.zycie-=obojentne
        if self.zycie<0:
            self.zycie=0

    def odswiez_moc(self,koszt):
        moc-=koszt
    
    def get_nazwe_zaklecia(self,ideks_zaklecia):
        return self.magic[ideks_zaklecia]["nazwa"]

    def get_koszt_zaklecia(self,ideks_zaklecia):
        return self.magic[ideks_zaklecia]["koszt"]

    def choose_action(self):
        i=1
        for item in self.action:
            print(str(i)," : ",item)
            i+=1
    
    def choose_magic(self):
        i=1
        for item in self.magic:
            print(str(i)," : Nazwa - ", item["nazwa"],"       Koszt - ",item["koszt"])
            i+=1
    