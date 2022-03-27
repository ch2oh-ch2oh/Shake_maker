import eel


@eel.expose
def convert_value_py(values):
    res = get_receipts(values)
    a = []
    for i in res:
        a.append(i.name)
    return a


cocktails = []


class Cocktail:
    def __init__(self, name, components, receipt, ingredients):
        self.name = name
        self.components = components
        self.receipt = receipt
        self.ingredients = ingredients


def read():
    with open("req.txt", 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:
                break
            name = line.strip('\n')
            components = []
            ingredients = set()
            for i in range(int(file.readline())):
                components.append(file.readline().strip('\n'))
                ingredients.add(components[i].split()[0].lower())
            receipt = file.readline().strip('\n')
            cocktails.append(Cocktail(name, components, receipt, ingredients))


def get_receipts(ingredients):
    receipts = dict()
    for cocktail in cocktails:
        a = cocktail.ingredients - set(ingredients)
        if len(a) <= 1:
            receipts[cocktail] = a
    return receipts
