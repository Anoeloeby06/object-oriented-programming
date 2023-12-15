import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar  # Import Calendar from tkcalendar module

window = tk.Tk()
window.configure(bg='#696969')
window.geometry("720x540")
window.resizable(False, True)
window.title("Form Login")

input_frame = ttk.Frame(window)
input_frame.pack(padx=40, pady=40, fill="x", expand=True)

# Components

# First Name
firstNameLabel = ttk.Label(input_frame, text="First Name")
firstNameLabel.pack(padx=5, pady=5, fill='x', expand=True)

firstName = tk.StringVar()
firstNameInput = ttk.Entry(input_frame, textvariable=firstName)
firstNameInput.pack(padx=5, pady=5, fill='x', expand=True)

# Last Name
lastNameLabel = ttk.Label(input_frame, text="Last Name")
lastNameLabel.pack(padx=5, pady=5, fill='x', expand=True)

lastName = tk.StringVar()
lastNameInput = ttk.Entry(input_frame, textvariable=lastName)
lastNameInput.pack(padx=5, pady=5, fill='x', expand=True)

# NIK
nikLabel = ttk.Label(input_frame, text="NIK")
nikLabel.pack(padx=5, pady=5, fill='x', expand=True)

nik = tk.StringVar()
nikInput = ttk.Entry(input_frame, textvariable=nik)
nikInput.pack(padx=5, pady=5, fill='x', expand=True)

# Alamat
alamatLabel = ttk.Label(input_frame, text="Alamat")
alamatLabel.pack(padx=5, pady=5, fill='x', expand=True)

alamat = tk.StringVar()
alamatInput = ttk.Entry(input_frame, textvariable=alamat)
alamatInput.pack(padx=5, pady=5, fill='x', expand=True)

# Tanggal Lahir
tanggalLahirLabel = ttk.Label(input_frame, text="Tanggal Lahir")
tanggalLahirLabel.pack(padx=5, pady=5, fill='x', expand=True)

tanggalLahirCal = Calendar(input_frame, selectmode="day", year=2000, month=1, day=1)
tanggalLahirCal.pack(padx=5, pady=5, fill='x', expand=True)

# Nama Ayah
namaAyahLabel = ttk.Label(input_frame, text="Nama Ayah")
namaAyahLabel.pack(padx=5, pady=5, fill='x', expand=True)

namaAyah = tk.StringVar()
namaAyahInput = ttk.Entry(input_frame, textvariable=namaAyah)
namaAyahInput.pack(padx=5, pady=5, fill='x', expand=True)

# Nama Ibu
namaIbuLabel = ttk.Label(input_frame, text="Nama Ibu")
namaIbuLabel.pack(padx=5, pady=5, fill='x', expand=True)

namaIbu = tk.StringVar()
namaIbuInput = ttk.Entry(input_frame, textvariable=namaIbu)
namaIbuInput.pack(padx=5, pady=5, fill='x', expand=True)

def buttonOnClick():
    if not firstName.get() or not lastName.get() or not nik.get() or not alamat.get() or not tanggalLahirCal.get_date() or not namaAyah.get() or not namaIbu.get():
        print("Please fill in all fields.")
    else:
        pesan = f"First Name: {firstName.get()}\n"
        pesan += f"Last Name: {lastName.get()}\n"
        pesan += f"NIK: {nik.get()}\n"
        pesan += f"Alamat: {alamat.get()}\n"
        pesan += f"Tanggal Lahir: {tanggalLahirCal.get_date()}\n"
        pesan += f"Nama Ayah: {namaAyah.get()}\n"
        pesan += f"Nama Ibu: {namaIbu.get()}\n"
        print(pesan)

submit_button = ttk.Button(input_frame, text="Submit", command=buttonOnClick)
submit_button.pack(pady=10)

window.mainloop()