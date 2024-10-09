class Gramatas:
    def __init__ (self, nosaukums, autors, irIzsniegta, izsniegšanas_datums, nodošanas_datums):
        self.nosaukums = nosaukums
        self.autors = autors
        self.irIzsniegta = False
        self.izsniegšanas_datums = None
        self.nodosanas_datums = None
    def __repr__ (self):
        return f"Gramata: {self.nosaukums}, {self.autors}, {self.irIzsniegta}, {self.izsniegšanas_datums}, {self.nodosanas_datums}"

class IzsniegsanasSaraksts:
    def __init__(self):
        self.gramatas = []
    
    def izsniegt_gramatu(self, gramata):
        self.gramatas.append(gramata)
        self.gramatas[-1].irIzsniegta = True
        self.gramatas[-1].izsniegšanas_datums = f"2022-10-20"
        self.gramatas[-1].nodosanas_datums = f"2022-10-24"

saraksts = IzsniegsanasSaraksts()
gramata = Gramatas("Book1", "Author1", False, None, None)
saraksts.izsniegt_gramatu(gramata)
print(saraksts.gramatas)

'''
4. uzdevums
from datetime import datetime, timedelta

class Gramata:
    def __init__(self, nosaukums, autors):
        self.nosaukums = nosaukums
        self.autors = autors
        self.irIzsniegta = False
        self.izsniegsanas_datums = None
        self.nodosanas_datums = None

class IzsniegsanasSaraksts:
    def __init__(self):
        self.gramatas = []

    def pievienot_gramatu(self, gramata):
        self.gramatas.append(gramata)

    def izsniegt_gramatu(self, nosaukums):
        for gramata in self.gramatas:
            if gramata.nosaukums == nosaukums and not gramata.irIzsniegta:
                gramata.irIzsniegta = True
                gramata.izsniegsanas_datums = datetime.now()
                gramata.nodosanas_datums = datetime.now() + timedelta(days=14)
                return f"Grāmata '{nosaukums}' izsniegta."
        return "Grāmata nav pieejama vai jau ir izsniegta."

    def atgriezt_gramatu(self, nosaukums):
        for gramata in self.gramatas:
            if gramata.nosaukums == nosaukums and gramata.irIzsniegta:
                gramata.irIzsniegta = False
                gramata.izsniegsanas_datums = None
                gramata.nodosanas_datums = None
                return f"Grāmata '{nosaukums}' atgriezta."
        return "Grāmata netika atrasta."

    def meklet_izsniegtas_gramatas(self):
        return [g.nosaukums for g in self.gramatas if g.irIzsniegta]

# Testēšana
biblioteka = IzsniegsanasSaraksts()
gramata1 = Gramata("Dzintara ceļš", "Mārtiņš Ziedonis")
gramata2 = Gramata("Zem ūdens", "Anna Lāce")

biblioteka.pievienot_gramatu(gramata1)
biblioteka.pievienot_gramatu(gramata2)

print(biblioteka.izsniegt_gramatu("Dzintara ceļš"))
print(biblioteka.meklet_izsniegtas_gramatas())
print(biblioteka.atgriezt_gramatu("Dzintara ceļš"))
'''