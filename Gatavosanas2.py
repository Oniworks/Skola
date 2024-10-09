from abc import ABC, abstractmethod

class Transportlidzeklis(ABC):
    @abstractmethod
    def aprekina_nobraukumu(self):
        pass

class Automasina(Transportlidzeklis):
    def __init__(self, degvielas_tilpums, patēriņš):
        self.degvielas_tilpums = degvielas_tilpums
        self.patēriņš = patēriņš

    def aprekina_nobraukumu(self):
        return self.degvielas_tilpums / self.patēriņš * 100

class Velosipeds(Transportlidzeklis):
    def __init__(self, attalums):
        self.attalums = attalums

    def aprekina_nobraukumu(self):
        return self.attalums

# Testēšana
transporti = [Automasina(50, 5), Velosipeds(30)]

for transports in transporti:
    print(f"Nobraukums ir: {transports.aprekina_nobraukumu()} km")