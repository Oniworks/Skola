class Reservacijas:
    def __init__(self, klienta_vards, galamerkis, datums, rezervacijas_nummurs):
        self.klienta_vards = klienta_vards
        self.galamerkis = galamerkis
        self.datums = datums
        self.rezervacijas_nummurs = rezervacijas_nummurs
        self.statuss = "rezervēts"
        #statuss = rezervēts, apmaksāts, atcelts.
    def atcelt_rezervaciju(self):
        self.statuss = "atcelts"
        print(f"{self.klienta_vards}, rezervācija ar nummuru {self.rezervacijas_nummurs} ir atcelta")

class Agentura:
    def __init__(self):
        self.rezervacijas = []
    def pievienot_rezervaciju(self, rezervacija):
        self.rezervacijas.append(rezervacija)
        print(f"{rezervacija.klienta_vards} ar rezervācijas ar nummuru {rezervacija.rezervacijas_nummurs} ir pievienots")
    def paradit_visas_rezervacijas(self):
        return [r.__dict__ for r in self.rezervacijas]

    def meklet_pec_klienta(self, klienta_vards):
        return [r for r in self.rezervacijas if r.klienta_vards == klienta_vards]

Menedzesana = Agentura()
Janis = Reservacijas("Jānis Bērziņš", "Budapešta", "10.10.24.", 1224)
Peters = Reservacijas("Pēteris Liepiņš", "Kanāda", "11.09.25.", 1324)

Menedzesana.pievienot_rezervaciju(Janis)
Menedzesana.pievienot_rezervaciju(Peters)

print(Menedzesana.paradit_visas_rezervacijas())
print(Menedzesana.meklet_pec_klienta("Jānis Bērziņš"))