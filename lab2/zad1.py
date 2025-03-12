from defs_zad1 import *

class DecisionSystem:

    def __init__(self, data):
        self.data = data
        self.reguly = []
        self.reguly_2 = []
        self.obiekty_pokryte = set()



data = wczytaj('values.txt')

system = DecisionSystem(data)
system.generate_reguly()
system.generate_reguly_2()
system.display_reguly()
