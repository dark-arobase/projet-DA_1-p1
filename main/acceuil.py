import tkinter as tk

def creer_accueil_utilisateur(root, retour=None):
    frame = tk.Frame(root, bg="black")

    label = tk.Label(frame, text="Bienvenue utilisateur", font=("Arial", 24), bg="black", fg="white")
    label.pack(pady=50)

    if retour:
        def deconnexion():
            frame.pack_forget()        # Cacher ce frame
            retour.pack(fill="both", expand=True)  # Afficher le frame de retour

        tk.Button(frame, text="Déconnexion", command=deconnexion).pack(pady=20)

    return frame
