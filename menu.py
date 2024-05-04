from Kredyty import kredyty


def menu():
    while True:
        print("\nMenu główne")
        print("1. Kredyty", "2. Pożyczki", "3. Raty", "4. Inne wydatki", "5. Koniec programu", sep="\n" )

        wybor = int(input("Jakiego wyboru chcesz dokonać?: "))
        if (wybor == 1):
            kredyty.kredyty()
        elif (wybor == 2):
            print("Będzie info o ratach")
        elif (wybor == 3):
            pass
        elif (wybor == 4):
            pass
        elif (wybor == 5):
            print("Dziękuje za skorzystanie z programu")
            break
        else:
            print("Podałeś niewłaściwy numer")