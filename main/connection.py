import tkinter as tk
import os
import acceuil


def connexion_utilisateur(root, retour=None):
    """Crée la frame de connexion utilisateur."""
    frame = tk.Frame(root, bg="black")
    root.title("Connexion")
    box_text_font = ("Arial", 12)

    tk.Label(frame, text="PAGE CONNEXION", font=("Arial", 24, "bold"),
             bg="black", fg="white").pack(pady=40)
    
    # Champ Nom
    tk.Label(frame, text="Nom d'utilisateur :", bg="black", font=box_text_font, fg="white").pack(pady=5)
    entry_nom = tk.Entry(frame, font=box_text_font)
    entry_nom.pack(pady=5)

    # Champ Email
    tk.Label(frame, text="Email :", bg="black", font=box_text_font, fg="white").pack(pady=5)
    entry_email = tk.Entry(frame, font=box_text_font)
    entry_email.pack(pady=5)

    # Champ Mot de passe
    tk.Label(frame, text="Mot de passe :", bg="black", font=box_text_font, fg="white").pack(pady=5)
    entry_mdp = tk.Entry(frame, font=box_text_font, show="*")
    entry_mdp.pack(pady=5)

    # Message d'erreur / succès
    label_message = tk.Label(frame, text="", font=box_text_font, fg="red", bg="black")
    label_message.pack(pady=10)

    def valider_connexion():
        nom = entry_nom.get().strip()
        email = entry_email.get().strip()
        mdp = entry_mdp.get().strip()

        if not nom or not email or not mdp:
            label_message.config(text="Veuillez remplir tous les champs.", fg="red")
            return

        fichier = "main/data/BasedeDonnee.csv"
        if not os.path.exists(fichier):
            label_message.config(text="Aucun utilisateur trouvé.", fg="red")
            return

        success = False
        with open(fichier, "r", encoding="utf-8") as f:
            for ligne in f:
                parts = ligne.strip().split(",")
                if len(parts) < 3:
                    continue
                nom_enr, email_enr, mdp_enr = parts[:3]
                if nom == nom_enr and email == email_enr and mdp == mdp_enr:
                    success = True
                    break

        if success:
            label_message.config(text="Connexion réussie !", fg="green")
            frame.after(1000, lambda: changer_page(frame, acceuil.creer_accueil_utilisateur(root,nom, retour=frame)))
        else:
            label_message.config(text="Nom, Email ou mot de passe incorrect.", fg="red")

    # Bouton Connexion
    tk.Button(frame, text="Connexion", command=valider_connexion,
              bg="white", fg="black", font=("Arial", 12, "bold")).pack(pady=20)

    # Bouton Retour
    if retour:
        tk.Button(frame, text="Retour",
                  command=lambda: changer_page(frame, retour),
                  bg="white", fg="black", font=("Arial", 12, "bold")).pack(pady=10)

    return frame


def changer_page(frame_actuel, frame_suivant):
    frame_actuel.pack_forget()
    frame_suivant.pack(fill="both", expand=True)


# Mode test autonome
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")
    root.configure(bg="black")
    frame_connexion = connexion_utilisateur(root)
    frame_connexion.pack(fill="both", expand=True)
    root.mainloop()
