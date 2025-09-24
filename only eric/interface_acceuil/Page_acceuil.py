import tkinter as tk

# Fonction pour gérer les clics sur les boutons
def on_nav_click(name):
    print(f"Navigation : {name}")

def on_main_button_click(name):
    print(f"Action : {name}")

# Création de la fenêtre principale
root = tk.Tk()
root.title("Interface Quiz Admin")
root.geometry("800x600")
root.configure(bg="white")

# ------------------------------
# BARRE DE NAVIGATION EN HAUT
# ------------------------------
navbar = tk.Frame(root, bg="black", height=50)
navbar.pack(fill="x")

# Boutons de navigation
nav_buttons = ["Accueil", "Explorer", "Mode utilisateur"]
for text in nav_buttons:
    btn = tk.Button(navbar, text=text, command=lambda t=text: on_nav_click(t),
                    bg="black", fg="white", relief="flat", padx=20, pady=10)
    btn.pack(side="left", padx=5, pady=5)

# Espace utilisateur (à droite)
user_frame = tk.Frame(navbar, bg="black")
user_frame.pack(side="right", padx=10)

user_label = tk.Label(user_frame, text="Nom utilisateur (admin)", fg="white", bg="black")
user_label.pack(side="left", padx=5)

# (Optionnel) Ajout d'un avatar (image) : ici, juste un rond gris simulé
avatar = tk.Canvas(user_frame, width=30, height=30, bg="black", highlightthickness=0)
avatar.create_oval(5, 5, 25, 25, fill="gray")
avatar.pack(side="left")

Label = tk.Label(root, text="Bienvenue sur Yuppiquiz!", font=("Arial", 24, "bold"), fg="Orange", bg="aqua")
Label.pack(pady=20)

# ------------------------------
# CONTENU PRINCIPAL
# ------------------------------
main_frame = tk.Frame(root, bg="white")
main_frame.pack(expand=True)

# Liste des boutons dans la zone centrale
actions = [
    ("Créé votre quiz", 0, 0),
    ("Modification d’un quiz", 0, 1),
    ("Explorer d’autre quiz", 1, 0),
    ("Hoster votre quiz", 1, 1)
]

for text, row, col in actions:
    btn = tk.Button(main_frame, text=text, command=lambda t=text: on_main_button_click(t),
                    bg="black", fg="white", font=("Arial", 12, "bold"), width=20, height=3)
    btn.grid(row=row, column=col, padx=40, pady=30)

# Centrage
main_frame.grid_rowconfigure((0, 1), weight=1)
main_frame.grid_columnconfigure((0, 1), weight=1)

# ------------------------------
# Lancement de la boucle principale
# ------------------------------
root.mainloop()
