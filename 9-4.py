#Message Error

print('Ini Adalah Pembagian\n\n')

while True:
    try:
        penyebut = int(input('Penyebut = '))
        pembilang = int(input('Pembilang = '))
        hasil = penyebut/pembilang
        break
    
    except ValueError:
        print('Yang Anda Masukkan Bukan sebuah Angka !')

    except ZeroDivisionError:
        print('Angka Pembilang Adalah 0\nError 404')

    except Exception as err:
        print(err)

    finally:
        print(f'Hasil = {hasil}')