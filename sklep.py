class Sklep:
    def __init__(self):
        self.produkty = []

    def dodaj_produkt(self, produkt):
        self.produkty.append(produkt)

    def pokaz_magazyn(self):
        print("\n--- STAN MAGAZYNU ---")
        for p in self.produkty:
            p.pokaz_info()
        print("---------------------")

    def znajdz_produkt(self, szukane_id):
        for p in self.produkty:
            if p.id_produktu == szukane_id:
                return p
        return None