class SecurePlant:
    def __init__(self, name, age, height):
        self.__name = name
        self.__age = age
        self.__height = height

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age
    
    @property
    def height(self):
        return self.__height

    @name.setter
    def name(self, name):
        self.__name = name

    @name.setter
    def age(self, age):
        if age > 0:
            self.__age = age
            print(f"Age updated {self.__age} [OK]")
        else:
            print("Age must be positive")

    @name.setter
    def height(self, height):
        if height > 0:
            self.__height = height
            print(f"Height updated {self.__height} [OK]")
        else:
            print("Height must be positive")

    def __str__(self):
        return f"{self.__name} : ({self.__height} cm, {self.__age} days old)"

    def grow(self):
        self.__age += 1

    def Age(self):
        self.height += 1

    def get_info(self):
        print(f"{self.name} : {self.height} cm {self.age} days old")

class Flower(SecurePlant):
    def __init__(self, name, age, height, color):
        super().__init__(name, age, height)
        self.color = color

    def bloom(self):
        print(f"{self.name} is blooming beautifully")

    def __str__(self):
        return f"{self.name} ({self.__class__.__name__}) : {self.height} cm, {self.age}, {self.color} red"


class Tree(SecurePlant):
    def __init__(self, name, age, height, trunk_diameter):
        super().__init__(name, age, height)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        print(f"{self.name} provides {self.trunk_diameter} square meters of shade")

    def __str__(self):
        return f"{self.name} ({self.__class__.__name__}) : {self.height} cm, {self.age}, {self.trunk_diameter} diameter"


class Vegetable(SecurePlant):
    def __init__(self, name, age, height, harvest_season, nutritional_value):
        super().__init__(name, age, height)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_info(self):
        print(f"{self.name} is rich in vitamine {self.nutritional_value}")

    def __str__(self):
        return f"{self.name} ({self.__class__.__name__}) : {self.height} cm, {self.age}, {self.harvest_season}"


if __name__ == "__main__":
    print("=== Garden Types ===")
    flower = Flower("Rose", 30, 25, "red")
    print(flower)
    flower.bloom()
    tree = Tree("Oak", 1825, 500, 50)
    print(tree)
    tree.produce_shade()
    vegetable = Vegetable("Tomato", 90, 80, "summer harvest", "C")
    print(vegetable)
    vegetable.get_info()
