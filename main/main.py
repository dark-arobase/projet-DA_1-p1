import tkinter as tk

import connection
import inscription

# -------------------
# Fenêtre principale
# -------------------
root = tk.Tk()
root.title("Yuppiquiz")
root.geometry("800x600")
root.configure(bg="black")

# -------------------
# Gestion des frames
# -------------------
def afficher_frame(frame):
    for f in (frame_accueil, frame_inscription, frame_connexion):
        f.pack_forget()
    frame.pack(fill="both", expand=True)

# -------------------
# Page Accueil
# -------------------
frame_accueil = tk.Frame(root, bg="black")

# Frame centrale avec rectangle blanc
frame_centre = tk.Frame(frame_accueil, bg="black", width=450, height=450, highlightbackground="white",
                        highlightthickness=2)
frame_centre.place(relx=0.5, rely=0.5, anchor="center")

tk.Label(frame_centre, text="Bienvenue sur Yuppiquiz !", bg="black", fg="white",
         font=("Arial", 18, "bold")).pack(pady=(40, 10))

tk.Label(frame_centre, text="Testez vos connaissances et amusez-vous.", bg="black", fg="white",
         font=("Arial", 12)).pack(pady=(0, 30))

tk.Button(frame_centre, text="INSCRIPTION",
          command=lambda: afficher_frame(frame_inscription),
          bg="white", fg="black", font=("Arial", 12, "bold")).pack(pady=10)

tk.Button(frame_centre, text="SE CONNECTER",
          command=lambda: afficher_frame(frame_connexion),
          bg="white", fg="black", font=("Arial", 12, "bold")).pack(pady=10)

# -------------------
# Créer frames via modules
# -------------------
frame_inscription = inscription.creer_inscription(root, retour=frame_accueil)
frame_connexion = connection.connexion_utilisateur(root, retour=frame_accueil)

# -------------------
# Lancer sur la page accueil
# -------------------
afficher_frame(frame_accueil)

root.mainloop()
