class Bankaskonts:
    def __init__(self, ipasnieks, bilance):
        self.ipasnieks = ipasnieks
        self.bilance = bilance
    def paradit_bilanci(self):
        print(f"Konta atlikums: {self.bilance}")
    def ieskaitit(self, summa):
        self.bilance = self.bilance + summa
        print(f"Jaunais konta atlikums: {self.bilance}")
    def iznemt(self, summa):
        if self.bilance >= summa:
            self.bilance = self.bilance - summa
            print(f"Jaunais konta atlikums: {self.bilance}")
        elif self.bilance < summa:
            print("Tu pārāk broke, ej pelni naudu labāk.")
        else:
            print("Error")

ipasnieks1 = input("Konta īpašnieks: ")
bilance1 = int(input("Kāda ir konta sākuma bilance: "))
konts1 = Bankaskonts(ipasnieks1, bilance1)

konts1.paradit_bilanci()

konts1.iznemt(int(input("Cik daudz vēlaties izņemt: ")))

konts1.ieskaitit(int(input("Cik vēlaties ieskaitīt: ")))

konts1.iznemt(int(input("Cik daudz vēlaties izņemt: ")))