#File Not Found Error

try:
    with open('Pertemuan 9/file.txt') as file:
        text_file = file.read()
        print(f'{text_file}\n'*200)

except FileNotFoundError as error_message:
    print('Tidak Ada File')