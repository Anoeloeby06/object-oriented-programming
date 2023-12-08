from abc import ABC, abstractmethod
import time

class HewanMamalia(ABC):
    def __init__(self, nama):
        self.nama = nama

    @abstractmethod
    def sifat(self):
        pass

class Umur(HewanMamalia):
    def sifat(self):
        umur = getattr(self, 'umur', None)
        if umur is not None:
            if umur < 3:
                return "Merengek"
            elif 3 < umur < 5:
                return "Mandiri"
            else:
                return "Membunuh"

# Dictionary Mamalia
dict_hewan = {
    "gajah": Umur("Gajah"),
    "singa": Umur("Singa"),
    "monyet": Umur("Monyet"),
    "sapi": Umur("Sapi"),
    "domba": Umur("Domba"),
    "kucing": Umur("Kucing")
}

while True:
    print('\n               ANIMAL CHALLENGE\n\n')
    nama_hewan = input("Nama Hewan : ")
    if nama_hewan.lower() in dict_hewan:
        try:
            umur_hewan = int(input("Umur       : "))
            time.sleep(3)
            try:
                hewan = dict_hewan[nama_hewan.lower()]
                hewan.umur = umur_hewan
                print(f"\n{hewan.nama} Bergerak {hewan.sifat()}")
                break
            except TypeError as message_error:
                print(f"Terjadi kesalahan : {message_error}")
        except ValueError:
            print("Umur harus berupa angka.")
    else:
        print(f"Tidak ada informasi untuk hewan dengan nama : {nama_hewan}")

print("\nSelesai")