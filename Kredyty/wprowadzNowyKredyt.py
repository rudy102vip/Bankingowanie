import json

nazwaBanku = {}

def wprowadzNowyKredyt():
    while True:
        wprowadzNazweBanku = (input("Wprowadz nazwe banku: "))
        wprowadzKwoteKredytu = int(input("Wprowadź kwotę kredytu: "))
        nazwaBanku[wprowadzNazweBanku] = wprowadzKwoteKredytu
        kontynuowac = input("Czy chcesz kontynuować? 1. TAK / 2. NIE\n")
        with open("kredyty.json", "w") as plik:
            json.dump(nazwaBanku, plik)
        if kontynuowac != "1":
            break
        elif kontynuowac == "2":
            break
        else:
            print("Odpowiedź musi być TAK / NIE")
