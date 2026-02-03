class Plant:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def __str__(self):
        return f"{self.name} : ({self.height} cm, {self.age} days old)"

    def grow(self):
        self.age += 1

    def Age(self):
        self.height += 1

    def get_info(self):
        print(f"{self.name} : {self.height} cm {self.age} days old")


if __name__ == "__main__":
    factory = []
    print("===Plant Factory Output ===")
    for i in range(1,10,2):
        factory.append(Plant(f"rose{i}", i, i))
    for plant in factory:
        print(f"Created: {plant}")
    print(f"Total plants in factory: {len(factory)}")