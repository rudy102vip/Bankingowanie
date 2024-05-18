import podgladWydatkow
from KreatorMiesiaca import kreatorMiesiaca
import losowanieNumerowLotto
from datetime import datetime

def menu():
    while True:
        print("\nMenu główne")
        print("1. Kreator miesiąca", "2. Podgląd wydatków", "3. Losowanie numerów lotto", "4. Sprawdź aktualną datę",
              "5. Koniec programu" , sep="\n" )

        wybor = int(input("Jakiego wyboru chcesz dokonać?: "))
        if wybor == 1:
            kreatorMiesiaca.kreatorMiesiaca()
        elif wybor == 2:
            podgladWydatkow.podgladWydatkow()
        elif wybor == 3:
            losowanieNumerowLotto.losowanieNumerowLotto(6, 49)
        elif wybor == 4:
            aktualnaData = datetime.now().date()
            print(aktualnaData)
        elif wybor == 5:
            print("Dziękuje za skorzystanie z programu")
            break
        else:
            print("Podałeś niewłaściwy numer")