import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("600x650")
root.resizable(False, False)

main_frame = ttk.Frame(root, padding=25)
main_frame.pack(fill="both", expand=True)