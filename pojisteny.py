# Reprezentuje jednoho pojištěného.
class Pojisteny():

    # Inicializuje pojištěného a provádí validaci vstupních údajů.
    def __init__(self, jmeno, prijmeni, vek, telefon):
        if not jmeno.isalpha():
            raise ValueError("Jméno může obsahovat pouze písmena.")
        if not prijmeni.isalpha():
            raise ValueError("Příjmení může obsahovat pouze písmena.")
        if vek <= 0:
            raise ValueError("Věk musí být kladné číslo.")
        if not telefon:
            raise ValueError("Telefon nesmí být prázdný.")
        if not telefon.isnumeric():
            raise ValueError("Telefonní číslo může obsahovat pouze číslice.")

        self.jmeno = jmeno.capitalize()
        self.prijmeni = prijmeni.capitalize()
        self.vek = vek
        self.telefon = telefon

    # Vrátí textovou reprezentaci pojištěného.
    def __str__(self):
        return (f"{self.jmeno} {self.prijmeni} {self.vek} {self.telefon}")
