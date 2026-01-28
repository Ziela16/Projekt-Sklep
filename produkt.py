class Produkt:
    def __init__(self, id_produktu, nazwa, cena):
        self.id_produktu = id_produktu
        self.nazwa = nazwa
        self.cena = cena

    def pokaz_info(self):
        print(f"Kod: {self.id_produktu} | Nazwa: {self.nazwa} | Cena: {self.cena} PLN")