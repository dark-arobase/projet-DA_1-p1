import tkinter as tk
from main.classe.createur import createur


#Fenetre principal root
root = tk.Tk()
root.title("Interface Quiz Admin")
root.geometry("800x600")
root.configure(bg="black")

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

user_label = tk.Label(user_frame, text="{}", fg="white", bg="black")
user_label.pack(side="left", padx=5)

# (Optionnel) Ajout d'un avatar (image) : ici, juste un rond gris simulé
avatar = tk.Canvas(user_frame, width=30, height=30, bg="black", highlightthickness=0)
avatar.create_oval(5, 5, 25, 25, fill="gray")
avatar.pack(side="left")

Label = tk.Label(root, text="Création du quiz", font=("Arial", 24, "bold"), fg="Orange", bg="aqua")
Label.pack(pady=20)

main_frame=tk.Frame(root, bg="white")



root.mainloop()