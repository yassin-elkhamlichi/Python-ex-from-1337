class SecurePlant:
    def __init__(self,name, age, height):
        self.__name = name
        self.__age = age
        self.__height = height


    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_height(self):
        return self.__height
    
    def set_name(self,name):
        self.__name = name
    def set_age(self,age):
        if age > 0:
            self.__age = age
            print(f"Age updated {self.__age} [OK]")
        else:
            print("Age must be positive")
    def set_height(self,height):
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


if __name__ == "__main__":
    plant = SecurePlant(f"rose", 12, 12)
    print("===Garden Security Output ===")
    plant.set_age(13)
    plant.set_height(13)
    print(plant)
    plant.set_age(-1)
    plant.set_height(-1)
    print(plant)
    