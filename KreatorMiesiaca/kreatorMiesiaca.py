import datetime
import json
from KreatorMiesiaca import nadpisywaniePliku
from datetime import datetime

okresRozliczeniowy = []
def kreatorMiesiaca():

    print("Witamy w kreatorze wydatków")
    aktualnaData = datetime.now().date()
    wyborRokRozliczeniowy = input("Krok 1: Wprowadź rok rozliczeniowy: ")

    #wtsawić wyjątek

    wyborMiesiacaRozliczenia = input("Krok 2: Wybierz miesiąc rozliczenia: ")


    okresRozliczeniowy.append((str(aktualnaData), wyborRokRozliczeniowy, wyborMiesiacaRozliczenia))

    while True:
        wpiszWydatek = input("Krok 3: Wprowadź nazwę wydatku: ")
        wpiszKwoteWydatku = input("Wprowadź kwotę wydatku: ")
        okresRozliczeniowy.append((wpiszWydatek, wpiszKwoteWydatku))

        czyChceszKontynowac = input("Czy chcesz kontynuować dodawanie wydatków? TAK / NIE :")
        while not (czyChceszKontynowac.upper() == "TAK" or czyChceszKontynowac.upper() == "NIE"):
            print("Wybrałeś złą opcję")
            czyChceszKontynowac = input("Czy chcesz kontynuować dodawanie wydatków? TAK / NIE :")

        if czyChceszKontynowac.upper() == "TAK":
            print("Kontynuuj dodawanie wydatków")
        elif czyChceszKontynowac.upper() == "NIE":
            print("Koniec dodawania wydatków.")
            break
    

    nazwaPlikuZapis = wyborMiesiacaRozliczenia + wyborRokRozliczeniowy
    sciezkaZapisuPliku = "ZapisanePliki/" + nazwaPlikuZapis + ".json"

    with open(sciezkaZapisuPliku, "w", encoding="utf-8") as plik:
            json.dump(okresRozliczeniowy, plik, ensure_ascii=False)











