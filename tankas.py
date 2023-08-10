
class Tankas:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.kryptis = "Šiaurė"
        self.suviai = {"Šiaurė": 0, "Pietūs": 0, "Vakarai": 0, "Rytai": 0}

    def pirmyn(self):
        self.y += 1
        self.kryptis = "Šiaurė"

    def atgal(self):
        self.y -= 1
        self.kryptis = "Pietūs"

    def kairen(self):
        self.x -= 1
        self.kryptis = "Vakarai"

    def desinen(self):
        self.x += 1
        self.kryptis = "Rytai"

    def sauti(self):
        self.suviai[self.kryptis] += 1

    def info(self):
        print("x:", self.x)
        print("y:", self.y)
        print("Kryptis:", self.kryptis)
        print("Šūviai:", sum(self.suviai.values()), self.suviai)