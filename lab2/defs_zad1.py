def czy_zgodne(self, reg):
        atr, value, decision, _ = reg
        for obj_id, obj in self.data.items():
            if obj_id in self.obiekty_pokryte:
                continue

            if obj[atr] == value and obj['d'] != decision:
                return False
        return True

def generate_reguly(self):
        for obj_id, obj in self.data.items():
            if obj_id in self.obiekty_pokryte:
                continue

            for atr, value in obj.items():
                if atr == 'd':
                    continue

                reg = (atr, value, obj['d'], obj_id)
                if self.czy_zgodne(reg):
                    self.reguly.append(reg)
                    self.obiekty_pokryte.add(obj_id)
                    break


def czy_zgodne_2(self, reg):
        (atr1, value1), (atr2, value2), decision, _ = reg
        for obj_id, obj in self.data.items():
            if obj_id in self.obiekty_pokryte:
                continue
            if obj[atr1] == value1 and obj[atr2] == value2 and obj['d'] != decision:
                return False
        return True

def generate_reguly_2(self):
        pozostale = {k: v for k, v in self.data.items() if k not in self.obiekty_pokryte}
        for obj_id, obj in pozostale.items():
            atrybuty = [atr for atr in obj if atr != 'd']
            for i in range(len(atrybuty)):
                for j in range(i + 1, len(atrybuty)):
                    atr1, atr2 = atrybuty[i], atrybuty[j]
                    reg = ((atr1, obj[atr1]), (atr2, obj[atr2]), obj['d'], obj_id)
                    if self.czy_zgodne_2(reg):
                        self.reguly_2.append(reg)
                        self.obiekty_pokryte.add(obj_id)
                        break
                else:
                    continue
                break

def display_reguly(self):
        print("Reguły pierwszego rzędu:")
        for reg in self.reguly:
            print(f"({reg[0]} = {reg[1]}) => (d = {reg[2]}) [obiekt {reg[3]}]")

        print("\nReguły drugiego rzędu:")
        for reg in self.reguly_2:
            print(f"({reg[0][0]} = {reg[0][1]}) ∧ ({reg[1][0]} = {reg[1][1]}) => (d = {reg[2]}) więc wyrzucamy [obiekt {reg[3]}]")


def wczytaj(filename):
    data = {}
    atrybuty = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'd']

    with open(filename, 'r') as file:
        lines = file.readlines()

    dane = [list(map(int, line.strip().split())) for line in lines]

    for i, values in enumerate(dane):
        data[f'o{i + 1}'] = {atr: values[j] for j, atr in enumerate(atrybuty)}

    return data