class Hero:

    def __init__(self, name, health, attackPower, armor):
        self.name = name
        self.health = health
        self.attackPower = attackPower
        self.armor = armor

    def serang(self,lawan):
        print(self.name + ' menyerang ' + lawan.name)
        lawan.diserang(self, self.attackPower)

    def diserang(self,lawan, attackPower_lawan):
        print(self.name + ' diserang ' + lawan.name)
        attack_diterima = attackPower_lawan/self.armor
        print('Serangan terasa : ' + str(attack_diterima))
        self.health -= attack_diterima
        print('darah ' + self.name + ' tersisa ' + str(self.health))

alucard = Hero('alucard', 100, 10, 5)
bruno = Hero('bruno', 110, 20, 10)

alucard.serang(bruno)
print('\n')
bruno.serang(alucard)
print('\n')
bruno.serang(alucard)
print('\n')
bruno.serang(alucard)