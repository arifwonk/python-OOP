class Hero: # Template

    # class variables
    jumlah = 0
    __privateJumlah = 0

    def __init__(self, name, health):
        self.name = name
        self.health = health

        # variable instance private (__)
        self.__private = "private" 
        # variable instance protected (_)
        self._protected = "protect"


alucard = Hero("Alucard", 100)

print(alucard.__dict__) 
print(alucard._protected)
alucard._protected ="test"
print(alucard.__dict__)


# print(Hero.__dict__)
# print(Hero.__privateJumlah)