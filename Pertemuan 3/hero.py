import random

class dadWeapon:
    def __init__(self, inputweapon, inputdamage):
        self.Weapon = inputWeapon
        self.Damage = inputDamage

    def randomWeapon(self):
        #choice = random.randint(1, 5)
        random_index = random.randint(0, len(self.Weapon) - 1)
        random_weapon = self.Weapon[random_index]

class Match:    
    def __init__(self, inputName, inputDamage):
        #self.name = 
        #self.damage = inputDamage
    
    #getter called Private
    #def getName(self):
        #return self.__Name
    #def getDamage(self):
        #return self.__Damage
    

    #setter called private    
    def determiner(self, health):
        damage = self.damage
        health = self.father_weapon(health)
        health_now = health - damage
        if health_now <= 0:
            print('K.O.\nAnda Mati!')
        elif 1 >= health_now <= 25:
            print('Anda Sekarat')
        else:
            print('Anda masih punya Harapan hidup :)')

    def father_weapon(self, health):
        random_choice = random.randint(1, 5)
        if random_choice == 1:
            print(f'NYAWA MU     = {health}')
            print(f'Senjata Ayah = {self.name}')
            print(f'Damage       = {self.damage}')
            health -= 70
        elif random_choice == 2:
            print(f'NYAWA MU     = {health}')
            print(f'Senjata Ayah = {self.name}')
            print(f'Damage       = {self.damage}')
            health -= 99
        elif random_choice == 3:
            print(f'NYAWA MU     = {health}')
            print(f'Senjata Ayah = {self.name}')
            print(f'Damage       = {self.damage}')
            health -= 60
        elif random_choice == 4:
            print(f'NYAWA MU     = {health}')
            print(f'Senjata Ayah = {self.name}')
            print(f'Damage       = {self.damage}')
            health -= 50
        elif random_choice == 5:
            print(f'NYAWA MU     = {health}')
            print(f'Senjata Ayah = {self.name}')
            print(f'Damage       = {self.damage}')
            health -= 35
        return health

dadWeapon = [
    {'Sarung Wadimor', 60},
    {'Ikat Pinggang Abah', 75},
    {'Kursi Hijau', 55},
    {'Sapu Lidi', 45},
    {'Swallow', 35}
]

print('LIST WEAPON KEBANGGAAN BAPAK : ')

def menu():
    Start = True
    while Start:
        print('================================ Welcome To Match ====================================')
        print('\n\n')
        print('Kondisi anda sekarang :')
        print('[1] Tidur Tempat Teman')
        print('[2] Pulang Maghrib')
        print('[3] Mecahin gelas')
        print('[4] Bolos Ngaji\n')
        condition = int(input('Kesalahan :'))
        if condition == 1:
            health = 55
            skin1.determiner(health)
        elif condition == 2:
            health = 80
            skin2.determiner(health)
        elif condition == 3:
            health = 70
            skin3.determiner(health)
        elif condition == 4:
            health = 95
            skin4.determiner(health)

#menu()

print("Randomly Chosen Weapon:", dedWeapon.random_weapon["name"])
print("Damage Value:", random_weapon["damage"])