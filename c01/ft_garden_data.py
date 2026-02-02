class Plant:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def __str__(self):
        print(f"{self.name} : {self.height} cm {self.age} days old")


if __name__ == "__main__":
    g1 = Plant("rose", 30, 25)
    g2 = Plant("sunflower", 45, 80)
    g3 = Plant("cactus", 45, 80)
    registry = [g1, g2, g3]

    print("======= Garden Plant Registry ========")
    for g in registry:
        g.__str__()

