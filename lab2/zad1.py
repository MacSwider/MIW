from defs_zad1 import *

data = wczytaj('values.txt')

system = DecisionSystem(data)
system.generate_reguly()
system.generate_reguly_2()
system.display_reguly()
