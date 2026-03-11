from pojisteny import Pojisteny
class Evidence:
#Eviduje seznam pojištěných
    def __init__(self):
        self.pojistenci = []

    def pridej_pojisteneho(self, pojisteny): #přidává nového pojištěnce
        self.pojistenci.append(pojisteny)

    def vypis_vsechny(self): # vypisuje seznam všech pojištěnců
        return self.pojistenci

    def vyhledej_pojisteneho(self, jmeno, prijmeni): #vyhledává v seznamu pojištěných podle jména a příjmení
        for pojisteny in self.pojistenci:
            if pojisteny.jmeno == jmeno and pojisteny.prijmeni == prijmeni:
                return pojisteny


