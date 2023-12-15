class Weapon: #Template
    jumlah_weapon = 0

    def __init__(self, inputName, inputDamage, inputRange):
        self.name = inputName
        self.damage = inputDamage
        self.range = inputRange

        Weapon.jumlah_weapon += 1
        print(f'Membuat Weapon dengan Nama : {self.name}')

    def void(self):
        print('Halo, ')

    def rangeup(self):
        self.range += up

    def getrange(self):
        return self.range

skin1 = Weapon('Sarung Gajah Duduk', 70, 45)
print(f'Jumlah Weapon = {Weapon.jumlah_weapon}\n')

skin2 = Weapon('Ikat Pinggang Abah', 99, 40)
print(f'Jumlah Weapon = {Weapon.jumlah_weapon}\n')

skin3 = Weapon('Kursi Hijau', 60, 85)
print(f'Jumlah Weapon = {Weapon.jumlah_weapon}\n')

skin4 = Weapon('Sapu Lidi', 60, 20)
print(f'Jumlah Weapon = {Weapon.jumlah_weapon}\n')

skin5 = Weapon('Swallow', 35, 75)
print(f'Jumlah Weapon = {Weapon.jumlah_weapon}\n')

print('LIST WEAPON KEBANGGAAN BAPAK : ')
print(skin1.__dict__)
print(skin2.__dict__)
print(skin3.__dict__)
print(skin4.__dict__)
print(skin5.__dict__)