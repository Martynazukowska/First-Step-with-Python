from classes.game import Osoba,bcolors
from classes.magic import Czar
from classes.Dzialania import wypisz

#czarna magia
fire= Czar("Fire",10,100,"black")
thunder=Czar("Thunder",10,124,"black")
blizzard=Czar("Blizzard",20,100,"black")
water=Czar("Water",1,10,"black")

#biała magia
lek= Czar("Cure",12,120,"white")
pigula=Czar("Cura",18,200,"white")


magic=[fire,thunder,blizzard,water,lek,pigula]

#gracze
player1=Osoba(460,65,60,34,magic)
wrog=Osoba(1000,65,45,25,[])

run=True

Enemy=0
pom=0


while run:
    if Enemy==0:
        print("\n")
        #wybór czy chcemy zaatakować czy zaczarować
        print("Twój ruch:")
        print("==================================")
        player1.choose_action()
        wybor=input("Twoj wybór to: ")
        pom=int(wybor)-1
        if pom>len(player1.action):
            print(bcolors.FAIL+"\n Blad w komendzie \n"+bcolors.ENDC)
            continue
        print("\n")
        print("Wybrales: ",wybor," : ", player1.action[pom],"\n")

        #Atak
        if pom==0:
            dmg=player1.losuj_obrazenie()
            #zadaj nasz atak 
            wrog.take_obrazenie(dmg)
            print("Zadaleś atak wrogowi o sile: ", dmg)
            print("Wartość życia wroga to: ", wrog.zycie)
            Enemy=1
        
        #Zaczarowanie
        elif pom==1:
            #wybór zaklęcia
            print("==================================")
            player1.choose_magic()
            wybor=input("Twoj wybór to: ")
            pom2=int(wybor)-1
            #jeśli zla wartość zaklecia
            if pom2>len(player1.magic):
                print(bcolors.FAIL+"\n Blad w komendzie \n"+bcolors.ENDC)
                continue
            print("\n")
            print("Wybrales: ",wybor," : ",player1.get_zaklecie(pom2).get_nazwe_zaklecia(),
                "    o koszcie   ",player1.get_zaklecie(pom2).get_koszt_zaklecia(),"\n")
            #czy możemy użyć tego zaklecia
            twoja_moc=player1.get_moc()
            if player1.get_zaklecie(pom2).get_koszt_zaklecia()<twoja_moc:
                dmg=player1.get_zaklecie(pom2).losuj_magic()

                if player1.get_zaklecie(pom2).get_type_zaklecia()=="black":
                    #zazaruj
                    player1.odswiez_moc(player1.get_zaklecie(pom2).get_koszt_zaklecia())
                    wrog.take_obrazenie(dmg)
                    print("Zaczarowales wrogowi oslabiajac go o : ", dmg)
                    print("Wartość życia wroga to: ", wrog.zycie)
                    Enemy=1
                elif player1.get_zaklecie(pom2).get_type_zaklecia()=="white":
                    #lecz
                    player1.odswiez_moc(player1.get_zaklecie(pom2).get_koszt_zaklecia())
                    player1.heal(dmg)
                    print("Zwiększyłeś swoje życie o : ", dmg)
                    print("Wartość twojego życia to: ", player1.zycie)
                    Enemy=1
            else:
                print(bcolors.FAIL+"\n Za mało mocy \n"+bcolors.ENDC)
                continue


    #ruch wroga
    elif Enemy==1:
        print("\n")
        print(bcolors.FAIL+bcolors.BOLD+"Jestes pod atakiem"+bcolors.ENDC)
        #jeśli atak odpowiada atakiem
        if pom<=1:
            dmg=wrog.losuj_obrazenie()
            player1.take_obrazenie(dmg)
            print("Wróg zaatakował z siłą: ", dmg, "   Twoje życie wynosi: ",player1.get_zycie())
            Enemy=0

    #wypisz sytuacje z życiami
    wypisz(wrog,player1)
    
    #Końcowe komunikaty
    if wrog.get_zycie()==0:
        print(bcolors.OKGREEN+"Wygrana"+bcolors.ENDC)
        run=False
    
    elif player1.get_zycie()==0:
        print(bcolors.FAIL+"Porażka"+bcolors.ENDC)
        run=False


        
            
            

    

