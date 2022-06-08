class animals:
    def __init__(self, name, age, health_level, happiness_level):
        self.name =name
        self.age = age
        self.health_level = health_level
        self.happiness_level = happiness_level

    def display_info(self):
        print(
            f"name:{self.name} happiness:{self.happiness_level} health:{self.health_level}")
        return self

    def feed(self):
        print(f"after feeding {self.type} {self.name}!!")
        self.health_level += 10
        self.happiness_level += 10
        return self


class polarـbear(animals):
    def __init__(self, name):
        super().__init__(name=name, age=0, health_level=30, happiness_level=30)
        self.type = "polarـbear"

    def hotـweather(self):
        print(f"{self.type} Adapting to a hot-weather by swimming.")
        return self


class lions(animals):
    def __init__(self, name):
        super().__init__(name=name, age=0, health_level=5, happiness_level=10)
        self.type = "lions"

    def hotـweather(self):
        print(f"{self.type} Adapting to a hot-weather by dying!!")
        return self


class tigers(animals):
    def __init__(self, name):
        super().__init__(name=name, age=0,  health_level=10, happiness_level=20)
        self.type = "tigers"

    def hotـweather(self):
        print(
            f"{self.type} Adapting to a heat by eating chicken icecream or bloody treat!!")
        return self


BERNARO = polarـbear("BERNARO").display_info(
).feed().display_info().hotـweather()
Rajah = tigers("Rajah").display_info().feed().display_info().hotـweather()
Nala = lions("Nala").display_info().feed().display_info().hotـweather()