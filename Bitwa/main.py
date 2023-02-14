from classes.game import Osoba,bcolors

#słownik do różnych zaklęc
magic= [{"nazwa": "Fire", "koszt": 10, "obrazenia": 60},
        {"nazwa": "Thunder", "koszt": 10, "obrazenia": 80},
        {"nazwa": "Blizzard", "koszt": 20, "obrazenia": 80},
        {"nazwa": "Water", "koszt": 1, "obrazenia": 10}]

player1=Osoba(460,65,60,34,magic)

wrog=Osoba(1200,65,45,25,magic)

run=True

#czerwony, pogrubiony tekst
print(bcolors.FAIL+bcolors.BOLD+"Jestes pod atakiem"+bcolors.ENDC)

while run:
    print("========================")
    player1.choose_action()
    wybor=input("Twoj wybór to: ")

    print("Wybrales: ",wybor)

    pom=int(wybor)-1

    player1.choose_magic()
    wybor=input("Twoj wybór to: ")

    print("Wybrales: ",wybor)

    pom2=int(wybor)-1

    run=False

