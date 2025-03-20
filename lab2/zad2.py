from defs_zad2 import *

data = wczytaj_dane('values.txt')

system = DecisionSystem(data)
system.generuj_reguly_exhaustive()
system.wyswietl_reguly()


