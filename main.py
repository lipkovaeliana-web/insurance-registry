from pojisteny import Pojisteny
from evidence import Evidence


class Main:
    def __init__(self):
        self.evidence = Evidence()

    def spust_menu(self):

        while True:
            print("""
            Evidence pojištěných
            1 – Přidat pojištěného
            2 – Vypsat všechny pojištěné
            3 – Vyhledat pojištěného
            4 – Konec
            """)
            volba = int(input())
            match volba:
                case 1:
                    jmeno = input("Zadejte jméno pojištěného: ")
                    prijmeni = input("Zadejte příjmení pojištěného: ")
                    telefon = input("Zadejte telefonní číslo pojištěného: ")
                    vek = int(input("Zadejte věk pojištěného"))
                    pojisteny = Pojisteny(jmeno,prijmeni,vek, telefon)
                    self.evidence.pridej_pojisteneho(pojisteny)
                    input("Vložení nového pojištěného se zdařilo. Pokračuj libovolnou klávesou...")
                case 2:
                    seznam = self.evidence.vypis_vsechny()
                    for pojisteny in seznam:
                       print(pojisteny)
                    input("Pokračuj libovolnou klávesou...")
                case 3:
                    jmeno = input("Zadejte jméno pojištěného: ")
                    prijmeni = input("Zadejte příjmení pojištěného: ")
                    vysledek = self.evidence.vyhledej_pojisteneho(jmeno, prijmeni)
                    if vysledek is not None:
                        print(vysledek)
                    else:
                        print("Pojištěný nebyl nalezen")
                   input("Pokračuj libovolnou klávesou...")
                case 4:
                    print("Děkujeme za použití evidence pojištěných. Přeji krásný den.")
                    break
                case _:
                    print("Neplatná volba.")

main = Main()
main.spust_menu()














