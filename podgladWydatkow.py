import os
def podgladWydatkow():
    sciezkaDoZapisanePliki = "ZapisanePliki/"
    plikiWKatalogu = os.listdir(sciezkaDoZapisanePliki)
    for pliki in plikiWKatalogu:
        print(pliki)
    wybierzPlikDoOdczytu = input("Wybierz plik do odczytu: ")
    if wybierzPlikDoOdczytu in plikiWKatalogu:
        pelnaSciezkaDoZapisuPliku = os.path.join(sciezkaDoZapisanePliki, wybierzPlikDoOdczytu)
        with open(pelnaSciezkaDoZapisuPliku, "r", encoding="utf-8") as plik:
            zawartoscPliku = plik.read()
            print(zawartoscPliku)
