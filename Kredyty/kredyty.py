from Kredyty.wprowadzNowyKredyt import wprowadzNowyKredyt

def kredyty():
    while True:
        print("\nMenu kredyty")
        print("1. Wprowadź nowy kredyt", "2. Sprawdź aktualne kredyty", "3. Sprawdź sumę kredytów" , "4. Powrót do menu głównego", sep="\n")
        wyborKredyty = input("Jaki wybór chcesz dokonać?: ")
        if wyborKredyty == "1":
           wprowadzNowyKredyt()


        elif wyborKredyty == "2":
             '''
             print(nazwaBanku)
             '''
        elif wyborKredyty == "3":
            '''
            sumaKredytow = sum(nazwaBanku.values())
            #print(f"Suma twoich kredytów wynosi {sumaKredytow}")
            '''
        elif wyborKredyty == "4":
            break
        else:
            print("Podałeś niewłaściwą opcję")
