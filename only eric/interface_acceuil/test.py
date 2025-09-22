import tkinter as tk
from tkinter import messagebox

# Fonctionnalités des menus
def nouvelle_fenetre():
    messagebox.showinfo("Nouveau", "Nouvelle fenêtre ouverte !")

def quitter():
    root.quit()

# Création de la fenêtre principale
root = tk.Tk()
root.title("Interface avec barre de navigation")
root.geometry("400x300")

# Création de la barre de menu
menu_bar = tk.Menu(root)

# === Menu "Fichier" ===
menu_fichier = tk.Menu(menu_bar, tearoff=0)
menu_fichier.add_command(label="Nouveau", command=nouvelle_fenetre)
menu_fichier.add_separator()
menu_fichier.add_command(label="Quitter", command=quitter)
menu_bar.add_cascade(label="Fichier", menu=menu_fichier)

# === Menu "Édition" ===
menu_edition = tk.Menu(menu_bar, tearoff=0)
menu_edition.add_command(label="Copier")
menu_edition.add_command(label="Coller")
menu_bar.add_cascade(label="Édition", menu=menu_edition)

# === Menu "Aide" ===
menu_aide = tk.Menu(menu_bar, tearoff=0)
menu_aide.add_command(label="À propos", command=lambda: messagebox.showinfo("À propos", "Exemple Tkinter"))
menu_bar.add_cascade(label="Aide", menu=menu_aide)

# Ajout de la barre de menu à la fenêtre
root.config(menu=menu_bar)

# Boucle principale
root.mainloop()
