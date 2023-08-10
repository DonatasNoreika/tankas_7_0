
class Tankas:
    def __init__(self):
        self.x = 0
        self.y = 0

    def pirmyn(self):
        self.y += 1

    def atgal(self):
        self.y -= 1

    def kairen(self):
        self.x -= 1

    def desinen(self):
        self.x += 1

    def info(self):
        print("x:", self.x)
        print("y:", self.y)