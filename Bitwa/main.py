from classes.game import Osoba,bcolors

#słownik do różnych zaklęc
magic= [{"nazwa": "Fire", "koszt": 10, "obrazenia": 100},
        {"nazwa": "Thunder", "koszt": 10, "obrazenia": 124},
        {"nazwa": "Blizzard", "koszt": 20, "obrazenia": 100},
        {"nazwa": "Water", "koszt": 1, "obrazenia": 10}]

player1=Osoba(460,65,60,34,magic)

wrog=Osoba(1200,65,45,25,magic)

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
        
        elif pom==1:
            #Zaczarowanie
            #wybór zaklęcia
            print("==================================")
            player1.choose_magic()
            wybor=input("Twoj wybór to: ")
            pom2=int(wybor)-1
            print("\n")
            print("Wybrales: ",wybor," : ",player1.get_nazwe_zaklecia(pom2),
                "    o koszcie   ",player1.get_koszt_zaklecia(pom2),"\n")
            #czy możemy użyć tego zaklecia
            twoja_moc=player1.get_moc()
            if player1.get_koszt_zaklecia(pom2)<twoja_moc:
                dmg=player1.losuj_magic(pom2)
                #zazaruj
                player1.odswiez_moc(player1.get_koszt_zaklecia(pom2))
                wrog.take_obrazenie(dmg)
                print("Zaczarowales wrogowi oslabiajac go o : ", dmg)
                print("Wartość życia wroga to: ", wrog.zycie)
                Enemy=1
            else:
                print(bcolors.FAIL+"\n Za mało mocy \n"+bcolors.ENDC)

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

        
        

    print("------------------------------------------")
    print("Wrog: "+bcolors.FAIL+str(wrog.get_zycie())+" na "+str(wrog.get_zycie_max())+bcolors.ENDC) 
    print("Ty: "+bcolors.OKGREEN+str(player1.get_zycie())+" na "+str(player1.get_zycie_max())+bcolors.ENDC) 
    print("    "+bcolors.OKGREEN+str(player1.get_moc())+" na "+str(player1.get_moc_max())+bcolors.ENDC) 
       
    if wrog.get_zycie()==0:
        print(bcolors.OKGREEN+"Wygrana"+bcolors.ENDC)
        run=False
    
    elif player1.get_zycie()==0:
        print(bcolors.FAIL+"Porażka"+bcolors.ENDC)
        run=False


        
            
            

    

