from classes.game import Osoba,bcolors

#słownik do różnych zaklęc
magic= [{"nazwa": "Fire", "koszt": 10, "obrazenia": 60},
        {"nazwa": "Thunder", "koszt": 10, "obrazenia": 80},
        {"nazwa": "Blizzard", "koszt": 20, "obrazenia": 80},
        {"nazwa": "Water", "koszt": 1, "obrazenia": 10}]

player1=Osoba(460,65,60,34,magic)

print(player1.losuj_obrazenie())
print(player1.losuj_magic(0))
print(player1.losuj_magic(1))
print(player1.losuj_magic(2))
print(player1.losuj_magic(3))