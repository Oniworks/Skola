class Gramata:
    def __init__(self, nosaukums, autors, lpp_skaits):
        self.nosaukums = nosaukums
        self.autors = autors
        self.lpp_skaits = lpp_skaits

    def paradit_info(self):
        print(f"Grāmata: {self.nosaukums}")
        print(f"Autors: {self.autors}")
        print(f"Lapaspušu skaits: {self.lpp_skaits}")

print("Ievadiet informāciju par pirmo grāmatu:")
# Iegūstam datus no lietotāja
nosaukums1 = input("Ievadiet nosaukumu: ")
autors1 = input("Ievadiet autoru: ")
# Svarīgi! input() atgriež tekstu, tāpēc tas jāpārveido par skaitli (int)
lpp1 = int(input("Ievadiet lappušu skaitu: "))

# Izveidojam pirmo 'Gramata' objektu, izmantojot ievadītos datus
gramata1 = Gramata(nosaukums1, autors1, lpp1)

# Izsaucam metodi pirmajam objektam
gramata1.paradit_info()