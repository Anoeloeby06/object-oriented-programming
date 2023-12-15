#Zero DIvision Error
input = int(input('Masukkan Input = '))

try:
    hasil = 10/input

except ZeroDivisionError:
    print("Nilai tidak dapat diproses")

print(input)