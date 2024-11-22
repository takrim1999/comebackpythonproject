class Human:
    def __init__(self, name, gender, age=0, hair="small", cloth=None):
        self.name = name
        self.age = age
        self.gender = gender
        self.hair = hair
        self.cloth = cloth

    def cut_hair(self):
        if self.hair == "long":
            self.hair = "medium"
        elif self.hair == "medium":
            self.hair = "small"
        elif self.hair == "small":
            self.hair = "bald"
        elif self.hair == "bald":
            print("no hair to cut!")
        else:
            print("Hair is not right!")

    def clothe(self, cloth):
        self.cloth = cloth

    def grow(self):
        self.age += 1
        if self.hair == "medium":
            self.hair = "long"
        elif self.hair == "small":
            self.hair = "medium"
        elif self.hair == "bald":
            self.hair = "small"
        elif self.hair == "long":
            pass
            # print("longer than long is also long!")
        else:
            print("Hair is not right!")

    def __str__(self):

        return f"""
                My name is {self.name}. I am {self.age} years old.
                My hair is {self.hair}. I'm currently wearing {self.cloth}
                """


prova = Human(name="Mehejabin Prova", gender="Female")
rupok = Human(name="Md. Takrim Ul Alam", gender="Male")


for i in range(20):
    prova.grow()
for i in range(25):
    rupok.grow()

prova.clothe("Three Piece")
rupok.clothe("Shirt-Trouser")
rupok.cut_hair()

print(prova)
print(rupok)
