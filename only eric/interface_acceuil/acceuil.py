import tkinter as tk

root = tk.Tk()
root.title("Accueil")
root.geometry("800x600")
root.configure(bg="black")
Label = tk.Label(root, text="Bienvenue sur Yuppiquiz!", font=("Arial", 24, "bold"), bg="black", fg="white")
Label.pack(pady=20)

root.mainloop()

