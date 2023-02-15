import random


class Czar:
    def __init__(self,nazwa,koszt,dmg,type):
        self.nazwa=nazwa
        self.koszt=koszt
        self.obrazenia=dmg
        self.type=type

    def get_nazwe_zaklecia(self):
        return self.nazwa
    
    def get_koszt_zaklecia(self):
        return self.koszt

    def get_obrazenia_zaklecia(self):
        return self.obrazenia

    def get_type_zaklecia(self):
        return self.type

    def losuj_magic(self):
        zaklecie_zakresD=self.obrazenia-10
        zaklecie_zakresG=self.obrazenia+10
        return random.randrange(zaklecie_zakresD,zaklecie_zakresG)

