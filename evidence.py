# Eviduje seznam pojištěných.
class Evidence:

    def __init__(self):
        self.pojistenci = []

    # Přidá nového pojištěného do evidence.
    def pridej_pojisteneho(self, pojisteny):
        self.pojistenci.append(pojisteny)

    # Vrátí seznam všech pojištěných v evidenci.
    def vypis_vsechny(self):
        return self.pojistenci

    # Vyhledá pojištěného podle jména a příjmení (nezávisle na velikosti písmen).
    def vyhledej_pojisteneho(self, jmeno, prijmeni):
        for pojisteny in self.pojistenci:
            if pojisteny.jmeno.lower() == jmeno.lower() and pojisteny.prijmeni.lower() == prijmeni.lower():
                return pojisteny
        return None

    # Zjistí, zda je seznam pojištěných prázdný.
    def je_prazdna(self):
        return len(self.pojistenci) == 0

