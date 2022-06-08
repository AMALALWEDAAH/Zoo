from animals import animals
from animals import lions
from animals import tigers
from animals import polarـbear


class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    def add_lion(self, name):
        self.animals.append(lions(name))

    def add_lion(self, name):
        self.animals.append(polarـbear(name))

    def add_tiger(self, name):
        self.animals.append(tigers(name))
        return self

    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()
        return self


zoo1 = Zoo("John's Zoo")
zoo1.add_lion("Nala")
zoo1.add_lion("Simba")
zoo1.add_tiger("Rajah")
zoo1.add_tiger("Shere Khan")
zoo1.print_all_info()

