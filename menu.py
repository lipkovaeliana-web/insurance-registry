# V menu probíhá komunikace s uživatelem.
from pojisteny import Pojisteny
from evidence import Evidence


class Menu:
    def __init__(self):
        self.evidence = Evidence()

    # Pozastaví program, dokud uživatel nestiskne Enter.
    def pokracuj(self):
        input("Pokračuj stisknutím klávesy Enter...")

    # Načte od uživatele jméno a příjmení.
    def nacti_jmeno_a_prijmeni(self):
        jmeno = input("Zadejte jméno pojištěného: ").strip()
        prijmeni = input("Zadejte příjmení pojištěného: ").strip()
        return jmeno, prijmeni

    # Spustí hlavní menu aplikace.
    def spust_menu(self):

        while True:
            print("""
            Evidence pojištěných
            1 – Přidat pojištěného
            2 – Vypsat všechny pojištěné
            3 – Vyhledat pojištěného
            4 – Konec
            """)

            try:
                # Ověří, že uživatel zadal číslo volby.
                volba = int(input())
            except ValueError:
                print("Zadejte číslo od 1 do 4.")
                continue

            match volba:
                case 1:
                    jmeno, prijmeni = self.nacti_jmeno_a_prijmeni()
                    telefon = input("Zadejte telefonní číslo pojištěného: ").strip()

                    try:
                        # Ověří, že věk byl zadán jako číslo.
                        vek = int(input("Zadejte věk pojištěného: "))
                        pojisteny = Pojisteny(jmeno, prijmeni, vek, telefon)
                        self.evidence.pridej_pojisteneho(pojisteny)
                        print("Vložení nového pojištěného se zdařilo.")
                    except ValueError as e:
                        # Vypíše chybu při neplatně zadaných údajích.
                        print(e)

                    self.pokracuj()

                case 2:
                    seznam = self.evidence.vypis_vsechny()

                    # Ošetření prázdného seznamu pojištěných.
                    if not seznam:
                        print("Seznam pojištěných je prázdný.")
                    else:
                        for pojisteny in seznam:
                            print(pojisteny)

                    self.pokracuj()

                case 3:
                    # Pokud je evidence prázdná, není v čem vyhledávat.
                    if self.evidence.je_prazdna():
                        print("Seznam pojištěných je prázdný.")
                    else:
                        jmeno, prijmeni = self.nacti_jmeno_a_prijmeni()
                        vysledek = self.evidence.vyhledej_pojisteneho(jmeno, prijmeni)

                        if vysledek is not None:
                            print(vysledek)
                        else:
                            print("Pojištěný nebyl nalezen.")

                    self.pokracuj()

                case 4:
                    print("Děkujeme za použití evidence pojištěných. Přeji krásný den.")
                    break

                case _:
                    # Ošetření neplatné volby menu.
                    print("Neplatná volba.")
                    self.pokracuj()






