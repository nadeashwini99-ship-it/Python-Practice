import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital Clock")
root.geometry("500x200")
root.resizable(False, False)

label = tk.Label(
    root,
    font=("Arial", 55, "bold"),
    background="black",
    foreground="white"
)

label.pack(anchor="center", fill="both", expand=True)

def update_time():
    current_time = strftime("%H:%M:%S")
    label.config(text=current_time)
    label.after(1000, update_time)

update_time()

root.mainloop()
