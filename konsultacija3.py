class Darbinieks:
    def __init__(self, vards, uzvards, nostradatas_stundas):
        self.vards = vards
        self.uzvards = uzvards
        self. nostradatas_stundas = nostradatas_stundas
    def apr_algu(self, likme):
        print("Alga ir: ")
        print(self.nostradatas_stundas * likme)
        print("\n")
    def radit_info(self):
        print(f"Vārds: {self.vards}")
        print(f"Uzvārds: {self.uzvards}")

class BirojaDarbinieks(Darbinieks):
    def __init__(self, vards, uzvards, nostradatas_stundas, kabineta_nummurs):
        super().__init__(vards, uzvards, nostradatas_stundas)
        self.kabineta_nummurs = kabineta_nummurs
    def radit_info(self):
        super().radit_info()
        print(f"Kabinets : {self.kabineta_nummurs}")
        print("\n")

class Programmetajs(Darbinieks):
    def __init__(self, vards, uzvards, nostradatas_stundas, programmesanas_valodas):
        super().__init__(vards, uzvards, nostradatas_stundas)
        self.programmesanas_valodas = programmesanas_valodas
    def radit_info(self):
        super().radit_info()
        print(f"Pārvalda : {self.programmesanas_valodas}")
        print("\n")

birojs1 = BirojaDarbinieks("Jānis", "Bērziņš", 40, "13.")
prog1 = Programmetajs("Jānis", "Liepiņš", 50, ["C++", "Python"])
birojs1.radit_info()
prog1.radit_info()
birojs1.apr_algu(10)
prog1.apr_algu(20)