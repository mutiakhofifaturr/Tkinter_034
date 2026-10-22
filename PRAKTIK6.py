import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("600x650")
root.resizable(False, False)

main_frame = ttk.Frame(root, padding=25)
main_frame.pack(fill="both", expand=True)

judul = ttk.Label(
    main_frame,
    text="APLIKASI PREDIKSI PRODI PILIHAN",
    font=("Arial", 16, "bold")
)
judul.pack(pady=(0, 10))

petunjuk = ttk.Label(
    main_frame,
    text="Masukkan nilai 10 mata pelajaran (0-100)"
)
petunjuk.pack(pady=(0, 15))

mata_pelajaran = [
    "Matematika",
    "Bahasa Indonesia",
    "Bahasa Inggris",
    "Informatika",
    "IPA",
    "IPS",
    "PPKn",
    "Pendidikan Agama",
    "Seni Budaya",
    "PJOK"
]

input_nilai = {}

form_frame = ttk.Frame(main_frame)
form_frame.pack()

for i, mapel in enumerate(mata_pelajaran):
    label = ttk.Label(form_frame, text=mapel, width=22)
    label.grid(row=i, column=0, padx=10, pady=5, sticky="w")

    entry = ttk.Entry(form_frame, width=25)
    entry.grid(row=i, column=1, padx=10, pady=5)

    input_nilai[mapel] = entry