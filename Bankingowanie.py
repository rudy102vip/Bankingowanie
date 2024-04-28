print("Bankingowanie ver.0.1")

nazwaBanku = {}


while True:
    print("1. Kredyty", "2. Pożyczki", "3. Raty", "4. Inne wydatki", "5. Koniec programu")
    wybor = input("Jakiego wyboru chcesz dokonać?: ")
    if (wybor == "1"):
        print("1. Wprowadź nowy kredyt", "2. Sprawdź aktualne kredyty")
        wyborKredyty = input("Jaki wybór chcesz dokonać?: ")
        if wyborKredyty == "1":
            wprowadzNazweBanku = input("Wprowadz nazwe banku: ")
            wprowadzKwoteKredytu = input("Wprowadź kwotę kredytu: ")
            nazwaBanku[wprowadzNazweBanku] = wprowadzKwoteKredytu
        elif (wyborKredyty == "2"):
            print(nazwaBanku)
        else:
            print("Podałeś niewłaściwą opcję")
    elif (wybor == "2"):
        pass
    elif (wybor == "3"):
        pass
    elif (wybor == "4"):
        pass
    elif (wybor == "5"):
        print("Dziękuje za skorzystanie z programu")
        break
    else:
        print("Podałeś niewłaściwy numer")

