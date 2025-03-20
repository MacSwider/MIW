class DecisionSystem:
    def __init__(self, data):
        self.data = data
        self.reguly = []
        self.macierz_nieodroznialnosci = self.stworz_macierz_nieodroznialnosci()

    def stworz_macierz_nieodroznialnosci(self):
        """Tworzy macierz nieodróżnialności, zapisując wspólne atrybuty dla obiektów o różnych decyzjach."""
        obiekty = list(self.data.keys())
        macierz = {obj: {} for obj in obiekty}

        for i in range(len(obiekty)):
            for j in range(i + 1, len(obiekty)):
                obj1, obj2 = obiekty[i], obiekty[j]
                if self.data[obj1]['d'] != self.data[obj2]['d']:
                    wspolne_atrybuty = []
                    for attr in self.data[obj1]:
                        if attr != 'd' and self.data[obj1][attr] == self.data[obj2][attr]:
                            wspolne_atrybuty.append(attr)

                    macierz[obj1][obj2] = wspolne_atrybuty
                    macierz[obj2][obj1] = wspolne_atrybuty

        return macierz

    def generuj_reguly_exhaustive(self):
        """Generuje reguły wyczerpujące zgodnie z macierzą nieodróżnialności."""
        uzyte_desygnatory = set()

        # Reguły pierwszego rzędu
        for obj, porownania in self.macierz_nieodroznialnosci.items():
            for porownany_obj, desygnatory in porownania.items():
                for desygnator in desygnatory:
                    reg = ((desygnator, self.data[obj][desygnator]), self.data[obj]['d'])
                    if reg not in uzyte_desygnatory:
                        self.reguly.append((reg, 1))
                        uzyte_desygnatory.add(reg)

        # Generowanie reguł wyższych rzędów
        self.generuj_reguly_wyzszych_rzedow(uzyte_desygnatory)

    def generuj_reguly_wyzszych_rzedow(self, uzyte_desygnatory):
        """Generuje reguły drugiego i wyższych rzędów."""
        for r in range(2, len(self.data[list(self.data.keys())[0]]) - 1):  # Kolejne rzędy reguł
            nowe_reguly = {}

            for obj, porownania in self.macierz_nieodroznialnosci.items():
                for porownany_obj, desygnatory in porownania.items():
                    if len(desygnatory) < r:
                        continue  # Jeśli za mało atrybutów, pomijamy

                    # Ręczne generowanie kombinacji zamiast itertools
                    kombinacje = []
                    for i in range(len(desygnatory)):
                        for j in range(i + 1, len(desygnatory)):
                            if r == 2:
                                kombinacje.append((desygnatory[i], desygnatory[j]))
                            else:
                                for k in range(j + 1, len(desygnatory)):
                                    kombinacje.append((desygnatory[i], desygnatory[j], desygnatory[k]))

                    for kombinacja in kombinacje:
                        reg = tuple((atr, self.data[obj][atr]) for atr in kombinacja)
                        decyzja = self.data[obj]['d']

                        if reg not in uzyte_desygnatory:
                            if reg in nowe_reguly:
                                nowe_reguly[reg][1] += 1  # Zwiększamy support
                            else:
                                nowe_reguly[reg] = [reg, 1, decyzja]

            # Dodanie nowych reguł do listy
            for reg_data in nowe_reguly.values():
                self.reguly.append((reg_data[0], reg_data[2], reg_data[1]))
                uzyte_desygnatory.add(reg_data[0])

    def wyswietl_reguly(self):
        """Wyświetla wygenerowane reguły."""
        print("Reguły wyczerpujące (exhaustive):")
        for reg in self.reguly:
            if isinstance(reg[0], tuple) and isinstance(reg[0][0], tuple):
                # Reguły wyższych rzędów
                desygnatory = " ∧ ".join([f"({atr} = {wartosc})" for atr, wartosc in reg[0]])
            else:
                # Reguły pierwszego rzędu
                desygnatory = f"({reg[0][0]} = {reg[0][1]})"

            print(f"{desygnatory} => (d = {reg[1]}) [support: {reg[2]}]")


def wczytaj_dane(filename):
    """Wczytuje dane z pliku."""
    data = {}
    atrybuty = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'd']

    with open(filename, 'r') as file:
        lines = file.readlines()

    for i, values in enumerate([list(map(int, line.strip().split())) for line in lines]):
        data[f'o{i + 1}'] = {atr: values[j] for j, atr in enumerate(atrybuty)}

    return data
