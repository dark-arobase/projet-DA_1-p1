import tkinter as tk

def creer_connexion(root, retour=None):
    """Crée la frame connexion."""
    frame = tk.Frame(root, bg="black")

    tk.Label(frame, text="PAGE CONNEXION", font=("Arial", 24, "bold"), bg="black", fg="white").pack(pady=40)

    tk.Label(frame, text="Nom d'utilisateur :", bg="black", font=("Arial", 12), fg="white").pack(pady=5)
    entry_nom = tk.Entry(frame, font=("Arial", 12))
    entry_nom.pack(pady=5)

    tk.Label(frame, text="Mot de passe :", bg="black", font=("Arial", 12), fg="white").pack(pady=5)
    entry_mdp = tk.Entry(frame, show="*", font=("Arial", 12))
    entry_mdp.pack(pady=5)

    def valider_connexion():
        print("Utilisateur :", entry_nom.get())
        print("Mot de passe :", entry_mdp.get())

    tk.Button(frame, text="Connexion", command=valider_connexion,
              bg="black", fg="white", font=("Arial", 12, "bold")).pack(pady=20)

    if retour:
        tk.Button(frame, text="Retour",
                  command=lambda: changer_page(frame, retour),
                  bg="black", fg="white", font=("Arial", 12, "bold")).pack(pady=10)

    return frame

def changer_page(frame_actuel, frame_suivant):
    frame_actuel.pack_forget()
    frame_suivant.pack(fill="both", expand=True)

# Mode test autonome
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")
    frame = creer_connexion(root)
    frame.pack(fill="both", expand=True)
    root.mainloop()
