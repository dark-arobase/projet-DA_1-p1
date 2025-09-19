import tkinter as tk

root = tk.Tk()
root.geometry("400x300")
root.title("Yuppiquiz")

# --------- Créer les 3 pages (frames) ---------
accueil = tk.Frame(root, bg="black")
connexion = tk.Frame(root, bg="white")
inscription = tk.Frame(root, bg="lightgray")

# --------- Contenu de la page Accueil ---------
tk.Label(accueil, text="Page d'accueil", fg="white", bg="black", font=("Arial", 16)).pack(pady=20)
tk.Button(accueil, text="Connexion", command=lambda: changer_page(connexion)).pack(pady=10)
tk.Button(accueil, text="Inscription", command=lambda: changer_page(inscription)).pack(pady=10)

# --------- Contenu de la page Connexion ---------
tk.Label(connexion, text="Page Connexion", bg="white", font=("Arial", 16)).pack(pady=20)
tk.Button(connexion, text="Retour", command=lambda: changer_page(accueil)).pack()

# --------- Contenu de la page Inscription ---------
tk.Label(inscription, text="Page Inscription", bg="lightgray", font=("Arial", 16)).pack(pady=20)
tk.Button(inscription, text="Retour", command=lambda: changer_page(accueil)).pack()

# --------- Fonction pour changer de page ---------
def changer_page(page):
    accueil.pack_forget()
    connexion.pack_forget()
    inscription.pack_forget()
    page.pack(fill="both", expand=True)

# --------- Démarrage : afficher l'accueil ---------
changer_page(accueil)

root.mainloop()
