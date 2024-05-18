from KreatorMiesiaca import kreatorMiesiaca
import os
def nadpisywaniePliku():
    miesiace = ["Styczeń", "Luty", "Marzec"]

    # Ścieżka do katalogu, w którym znajdują się pliki
    sciezka_do_katalogu = "ZapisanePliki/"

    # Sprawdzenie istnienia plików dla każdego miesiąca
    for miesiac in miesiace:
        nazwa_pliku = miesiac
        sciezka_do_pliku = os.path.join(sciezka_do_katalogu, nazwa_pliku)

        if os.path.exists(sciezka_do_pliku) and os.path.isfile(sciezka_do_pliku):
            print(f"Plik dla miesiąca {miesiac} istnieje.")
        else:
            print(f"Plik dla miesiąca {miesiac} nie istnieje.")