class Plant:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def __str__(self):
        return f"{self.name} : {self.height} cm {self.age} days old"

    def grow(self):
        self.age += 1

    def Age(self):
        self.height += 1

    def get_info(self):
        print(f"{self.name} : {self.height} cm {self.age} days old")


if __name__ == "__main__":
    g1 = Plant("rose", 30, 25)
    print("======= Day 1 ========")
    g1.get_info()
    old_val = g1.height
    for i in range(8):
        g1.Age()
        g1.grow()
        if i == 7:
            print("======= Day 7 ========")
            g1.get_info()
    print(f"Growth this week : {g1.height - old_val}")
