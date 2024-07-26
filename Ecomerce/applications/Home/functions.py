import tkinter as tk
from tkinter import messagebox
import time

class Cronometro:
    def __init__(self, root):
        self.root = root
        self.root.title("Cronómetro")
        self.root.geometry("300x150")
        
        self.time_var = tk.StringVar()
        
        self.label = tk.Label(root, text="Ingresa el tiempo en segundos:")
        self.label.pack(pady=10)
        
        self.entry = tk.Entry(root, textvariable=self.time_var)
        self.entry.pack(pady=5)
        
        self.start_button = tk.Button(root, text="Iniciar", command=self.start_cronometro)
        self.start_button.pack(pady=10)
        
        self.time_label = tk.Label(root, text="", font=("Helvetica", 24))
        self.time_label.pack(pady=10)
        
    def start_cronometro(self):
        try:
            total_time = int(self.time_var.get())
            self.countdown(total_time)
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa un número válido.")
    
    def countdown(self, remaining_time):
        if remaining_time >= 0:
            mins, secs = divmod(remaining_time, 60)
            time_format = f"{mins:02d}:{secs:02d}"
            self.time_label.config(text=time_format)
            self.root.update()
            self.root.after(1000, self.countdown, remaining_time - 1)
        else:
            messagebox.showinfo("Tiempo Finalizado", "¡El tiempo ha terminado!")

if __name__ == "__main__":
    root = tk.Tk()
    app = Cronometro(root)
    root.mainloop()
