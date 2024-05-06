import json
from Kredyty import kredyty
from KreatorMiesiaca import kreatorMiesiaca

def menu():
    while True:
        print("\nMenu główne")
        print("1. Kreator miesiąca", "2. Podgląd wydatków", "3. Koniec programu" , sep="\n" )

        wybor = int(input("Jakiego wyboru chcesz dokonać?: "))
        if wybor == 1:
            kreatorMiesiaca.kreatorMiesiaca()
        elif wybor == 2:
            with open("ZapisanePliki/Styczeń2024.json", "r", encoding="utf-8") as plik:
                dane_z_pliku = json.load(plik)
            print(dane_z_pliku)
        elif wybor == 3:
            print("Dziękuje za skorzystanie z programu")
            break
        else:
            print("Podałeś niewłaściwy numer")