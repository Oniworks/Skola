class Prece:
    def __init__(self, nosaukums, kategorija, cena):
        self.nosaukums = nosaukums
        self.kategorija = kategorija
        self.cena = cena

class Katalogs:
    def __init__(self):
        self.preces = []

    def pievienot_preces(self, prece):
        self.preces.append(prece)

    def dzest_preces(self, nosaukums):
        self.preces = [p for p in self.preces if p.nosaukums != nosaukums]

    def atjaunot_preces(self, nosaukums, jauna_cena):
        for prece in self.preces:
            if prece.nosaukums == nosaukums:
                prece.cena = jauna_cena

    def atrast_pec_kategorijas(self, kategorija):
        return [p for p in self.preces if p.kategorija == kategorija]

# Testēšana
katalogs = Katalogs()
prece1 = Prece("Ābols", "Augļi", 0.5)
prece2 = Prece("Grāmata", "Literatūra", 10)

katalogs.pievienot_preces(prece1)
katalogs.pievienot_preces(prece2)

print([p.nosaukums for p in katalogs.atrast_pec_kategorijas("Augļi")])