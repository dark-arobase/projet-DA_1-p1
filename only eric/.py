import tkinter as tk

def choix():
    print("Choix sélectionné :", var.get())

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Radiobutton sans valeur initiale")
fenetre.geometry("300x200")

# Variable partagée entre les boutons radio
var = tk.StringVar()

# Boutons radio
rb1 = tk.Radiobutton(fenetre, text="Chat", variable=var, value="chat")
rb2 = tk.Radiobutton(fenetre, text="Chien", variable=var, value="chien")
rb3 = tk.Radiobutton(fenetre, text="Oiseau", variable=var, value="oiseau")

# Placement dans la fenêtre
rb1.pack(anchor="w", padx=20, pady=5)
rb2.pack(anchor="w", padx=20, pady=5)
rb3.pack(anchor="w", padx=20, pady=5)

# Bouton pour valider le choix
btn = tk.Button(fenetre, text="Valider", command=choix)
btn.pack(pady=10)

# Lancer l'application
fenetre.mainloop()
