class Koszyk:
    def __init__(self):
        self.lista_zakupow = []

    def dodaj_do_koszyka(self, produkt):
        self.lista_zakupow.append(produkt)
        print(f"Dodano: {produkt.nazwa}")

    def podsumowanie(self):
        print("\n--- TWOJE ZAKUPY ---")
        suma = 0
        if not self.lista_zakupow:
            print("Koszyk jest pusty.")
        else:
            for p in self.lista_zakupow:
                print(f"- {p.nazwa} ({p.cena} PLN)")
                suma = suma + p.cena

            print(f"\nRAZEM DO ZAPLATY: {suma} PLN")
            print("--------------------")