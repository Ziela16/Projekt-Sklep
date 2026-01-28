from produkt import Produkt
from koszyk import Koszyk
from sklep import Sklep



moj_sklep = Sklep()

moj_sklep.dodaj_produkt(Produkt(1, "Mleko", 3.50))
moj_sklep.dodaj_produkt(Produkt(2, "Chleb", 4.20))
moj_sklep.dodaj_produkt(Produkt(3, "Maslo", 6.99))
moj_sklep.dodaj_produkt(Produkt(4, "Jajka (10szt)", 12.00))
moj_sklep.dodaj_produkt(Produkt(5, "Ser zolty", 8.50))
moj_sklep.dodaj_produkt(Produkt(6, "Szynka", 15.00))
moj_sklep.dodaj_produkt(Produkt(7, "Woda mineralna", 2.00))
moj_sklep.dodaj_produkt(Produkt(8, "Czekolada", 5.50))
moj_sklep.dodaj_produkt(Produkt(9, "Kawa", 25.00))
moj_sklep.dodaj_produkt(Produkt(10, "Żubr", 1000.99))



def menu():
    while True:
        print("\nWITAJ W SKLEPIE SPOZYWCZYM")
        print("1. Pokaz produkty")
        print("2. Zrob zakupy")
        print("3. Wyjdz")

        wybor = input("Wybierz opcje (1-3): ")

        if wybor == "1":
            moj_sklep.pokaz_magazyn()

        elif wybor == "2":
            moj_koszyk = Koszyk()
            print("\nRozpoczynamy zakupy! (Wpisz 0 zeby zakonczyc)")

            while True:
                try:
                    kod_str = input("Podaj kod produktu (barcode): ")
                    kod = int(kod_str)

                    if kod == 0:
                        break

                    znaleziony = moj_sklep.znajdz_produkt(kod)

                    if znaleziony is not None:
                        moj_koszyk.dodaj_do_koszyka(znaleziony)
                    else:
                        print("Nie ma takiego produktu!")
                except:
                    print("Blad! Wpisz poprawny numer.")

            moj_koszyk.podsumowanie()

        elif wybor == "3":
            print("Dziekujemy, zapraszamy ponownie!")
            break

        else:
            print("Nie ma takiej opcji.")

if __name__ == "__main__":
    menu()