import eel
import random


@eel.expose
def convert_value_py(ingredients):
    res = Cocktails()
    result = res.get_receipts(ingredients)

    a = []
    for i in result:
        a.append(i.name)
    return a


@eel.expose
def decorator_for_random_cocktail():
    return cocktails.get_random_receipt().name


def create_cocktails():
    global cocktails
    cocktails = Cocktails()


class Cocktails:

    def __init__(self):
        self.cocktails = []
        self.read()

    class Cocktail:
        def __init__(self, name, components, receipt, ingredients):
            self.name = name
            self.components = components
            self.receipt = receipt
            self.ingredients = ingredients

    def read(self):
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
                self.cocktails.append(self.Cocktail(name, components, receipt, ingredients))

    def get_receipts(self, ingredients):
        if type(ingredients) != list:
            return None
        for i in ingredients:
            if type(i) != str:
                return None
        receipts = []
        for cocktail in self.cocktails:
            insufficient = cocktail.ingredients - set(ingredients)
            if len(cocktail.ingredients) - len(insufficient) > 1:
                receipts.append([cocktail, len(insufficient)])
        receipts.sort(key=lambda x: x[1])
        return [x[0] for x in receipts]

    def get_random_receipt(self):
        return self.cocktails[random.randint(0, len(self.cocktails)) - 1]
