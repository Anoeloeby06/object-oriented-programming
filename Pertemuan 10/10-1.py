import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.configure(bg='#696969')
window.geometry("720x540")
window.resizable(True, False)
window.title("Form Login")

input_frame = ttk.Frame(window)
input_frame.pack(padx=10, pady=10, fill="x", expand=True)

# Component

firstNameLabel = ttk.Label(input_frame, text="First Name")
firstNameLabel.pack(padx=5, pady=5, fill='x', expand=True)

firstName = tk.StringVar()
firstNameInput = ttk.Entry(input_frame, textvariable=firstName)
firstNameInput.pack(padx=5, pady=5, fill='x', expand=True)

lastNameLabel = ttk.Label(input_frame, text="Last Name")
lastNameLabel.pack(padx=5, pady=5, fill='x', expand=True)

lastName = tk.StringVar()
lastNameInput = ttk.Entry(input_frame, textvariable=lastName)
lastNameInput.pack(padx=5, pady=5, fill='x', expand=True)

def buttonOnClick():
    pesan = f""

window.mainloop()