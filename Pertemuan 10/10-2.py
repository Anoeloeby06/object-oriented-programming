import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkcalendar import DateEntry

class BansosApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Form Bansos - 2023")
        self.master.geometry("550x700")
        self.master.resizable(False, False)
        self.master.configure(bg="Silver")

        self.setup_ui()

    def setup_ui(self):
        # Frame Utama
        main_frame = ttk.Frame(self.master)
        main_frame.pack(padx=20, pady=20, fill="both", expand=True)

        # Label "SISTEM"
        sistem_label = ttk.Label(main_frame, text="SISTEM", font=("Arial", 24, "bold"))
        sistem_label.grid(row=0, column=0, columnspan=2, pady=10, sticky="n")
        bansos_label = ttk.Label(main_frame, text="BANSOS - 2023", font=("Arial", 24, "bold"))
        bansos_label.grid(row=1, column=0, columnspan=2, pady=10, sticky="n")

        # Komponen - Label NIK
        nik_label = ttk.Label(main_frame, text="NIK", font=("Arial", 12))
        nik_label.grid(row=2, column=0, padx= 50, pady=10, sticky="w")

        self.NIK = tk.StringVar()
        nik_entry = ttk.Entry(main_frame, text=self.NIK, font=("Arial", 12))
        nik_entry.grid(row=2, column=1, padx= 50, pady=10, sticky="w")

        # Komponen - Label Nama Depan
        nama_depan_label = ttk.Label(main_frame, text="Nama Depan", font=("Arial", 12))
        nama_depan_label.grid(row=3, column=0, padx= 50, pady=10, sticky="w")

        self.NAMA_DEPAN = tk.StringVar()
        nama_depan_entry = ttk.Entry(main_frame, text=self.NAMA_DEPAN, font=("Arial", 12))
        nama_depan_entry.grid(row=3, column=1, padx= 50, pady=10, sticky="w")

        # Komponen - Label Nama Belakang
        nama_belakang_label = ttk.Label(main_frame, text="Nama Belakang", font=("Arial", 12))
        nama_belakang_label.grid(row=4, column=0, padx= 50, pady=10, sticky="w")

        self.NAMA_BELAKANG = tk.StringVar()
        nama_belakang_entry = ttk.Entry(main_frame, text=self.NAMA_BELAKANG, font=("Arial", 12))
        nama_belakang_entry.grid(row=4, column=1, padx= 50, pady=10, sticky="w")

        # Komponen - Label Alamat
        alamat_label = ttk.Label(main_frame, text="Alamat", font=("Arial", 12))
        alamat_label.grid(row=5, column=0, padx= 50, pady=10, sticky="w")

        self.ALAMAT = tk.StringVar()
        alamat_entry = ttk.Entry(main_frame, text=self.ALAMAT, font=("Arial", 12))
        alamat_entry.grid(row=5, column=1, padx= 50, pady=10, sticky="w")

        # Komponen - Label Tempat Tanggal Lahir
        tempat_lahir_label = ttk.Label(main_frame, text="Tempat Lahir", font=("Arial", 12))
        tempat_lahir_label.grid(row=6, column=0, padx= 50, pady=10, sticky="w")

        self.TEMPAT_LAHIR = tk.StringVar()
        tempat_lahir_entry = ttk.Entry(main_frame, text=self.TEMPAT_LAHIR, font=("Arial", 12))
        tempat_lahir_entry.grid(row=6, column=1, padx= 50, pady=10, sticky="w")

        tanggal_lahir_label = ttk.Label(main_frame, text="Tanggal Lahir", font=("Arial", 12))
        tanggal_lahir_label.grid(row=7, column=0, padx= 50, pady=10, sticky="w")

        self.TANGGAL_LAHIR = tk.StringVar()
        tanggal_lahir_cal = DateEntry(main_frame, textvariable=self.TANGGAL_LAHIR, date_pattern="dd-mm-yyyy", font=("Arial", 12))
        tanggal_lahir_cal.grid(row=7, column=1, padx= 50, pady=10, sticky="w")

        # Komponen - Label Nama Ayah
        nama_ayah_label = ttk.Label(main_frame, text="Nama Ayah", font=("Arial", 12))
        nama_ayah_label.grid(row=8, column=0, padx= 50, pady=10, sticky="w")

        self.NAMA_AYAH = tk.StringVar()
        nama_ayah_entry = ttk.Entry(main_frame, text=self.NAMA_AYAH, font=("Arial", 12))
        nama_ayah_entry.grid(row=8, column=1, padx= 50, pady=10, sticky="w")

        # Komponen - Label Nama Ibu
        nama_ibu_label = ttk.Label(main_frame, text="Nama Ibu", font=("Arial", 12))
        nama_ibu_label.grid(row=9, column=0, padx= 50, pady=10, sticky="w")

        self.NAMA_IBU = tk.StringVar()
        nama_ibu_entry = ttk.Entry(main_frame, text=self.NAMA_IBU, font=("Arial", 12))
        nama_ibu_entry.grid(row=9, column=1, padx= 50, pady=10, sticky="w")

        # Tombol - Tekan
        style = ttk.Style()
        style.configure("TButton",relief="flat", bg="#74D600")
        tombol_click = ttk.Button(main_frame, text="KIRIM", style="TButton", command=self.fungsi_click)
        tombol_click.grid(row=10, column=0, columnspan=2, pady=30)

    def fungsi_click(self):
        pesan = f"Data:\nNIK    : {self.NIK.get()}\nNama    : {self.NAMA_DEPAN.get()} {self.NAMA_BELAKANG.get()}\nAlamat    : {self.ALAMAT.get()}\nTempat Lahir : {self.TEMPAT_LAHIR.get()}\nTanggal Lahir  : {self.TANGGAL_LAHIR.get()}\nNama Ayah : {self.NAMA_AYAH.get()}\nNama Ibu  : {self.NAMA_IBU.get()}"
        showinfo(title="Informasi Data", message=pesan)

def main():
    root = tk.Tk()
    app = BansosApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()