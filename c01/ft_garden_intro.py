class Garden:
    def __init__(self, param1, param2, param3):
        self.name = param1
        self.age = param2
        self.height = param3


if __name__ == "__main__":
    g1 = Garden("rose", 30, 25)
    print("======= Welcome to My Garden========")
    print(f"Planet : {g1.name}")
    print(f"Height : {g1.height} cm")
    print(f"Age : {g1.age} days")
    print("======= End of Program========")
