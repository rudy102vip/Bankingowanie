import datetime
from Kredyty import kredyty
from KreatorMiesiaca import kreatorMiesiaca

def menu():
    while True:
        print("\nMenu główne")
        print("1. Kreator miesiąca", "2. Kredyty", "3. Pożyczki", "4. Raty", "5. Inne wydatki", "6. Koniec programu", sep="\n" )

        wybor = int(input("Jakiego wyboru chcesz dokonać?: "))
        if wybor == 1:
            kreatorMiesiaca.kreatorMiesiaca()
        elif wybor == 2:
            kredyty.kredyty()
        elif wybor == 3:
            print("Będzie info o ratach")
        elif wybor == 4:
            import datetime

            x = datetime.datetime(2024, 5, 5)

            print(x.strftime("%A"))

        elif wybor == 5:
            pass
        elif wybor == 6:
            print("Dziękuje za skorzystanie z programu")
            break
        else:
            print("Podałeś niewłaściwy numer")