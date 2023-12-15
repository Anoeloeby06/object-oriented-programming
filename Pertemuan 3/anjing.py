class Weapon: #Template
    def __init__(self, nama, umur, warna):
        self.name = nama
        self.umur = umur
        self.warna = warna

    def menggonggong(self):
        print('Panik ANJINGGGG!')

    def info(self):
        print(f'Nama Anjing = {self.name}, umur = {str(self.umur)} Tahun, Warna = {str(self.warna)}')
    
    def lari(self):
        print('RUN...................')

skin1 = Weapon('Sarung Gajah Duduk', 70, 45)
skin2 = Weapon('Sarung Gajah Duduk', 70, 45)
skin3 = Weapon('Sarung Gajah Duduk', 70, 45)
print(skin1.__dict__)
print(skin2.__dict__)
print(skin3.__dict__)