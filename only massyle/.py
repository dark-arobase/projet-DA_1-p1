import tkinter as tk
from PIL import Image, ImageTk

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
# Image de fond
# -------------------
img = Image.open("main/img/pattern.png")  # Assure-toi que le chemin est bon
photo = ImageTk.PhotoImage(img)

img_label = tk.Label(root, image=photo, bg="black")
img_label.image = photo  # Prévention du garbage collection
img_label.place(x=0, y=0, relwidth=1, relheight=1)  # L'image occupe tout l'écran

# -------------------
# Fonction pour basculer entre les frames
# -------------------
def afficher_frame(frame):
    for f in (frame_accueil, frame_inscription, frame_connexion):
        f.place_forget()
    frame.place(relx=0.5, rely=0.5, anchor="center")

# -------------------
# Frame ACCUEIL
# -------------------
frame_accueil = tk.Frame(root, width=400, height=400, bg="black", highlightthickness=2, highlightbackground="white")

# Contenu du frame accueil
tk.Label(frame_accueil, text="Bienvenue sur Yuppiquiz !", bg="black", fg="white",
         font=("Arial", 18, "bold")).pack(pady=(40, 10))

tk.Label(frame_accueil, text="Testez vos connaissances et amusez-vous.", bg="black", fg="white",
         font=("Arial", 12)).pack(pady=(0, 30))

tk.Button(frame_accueil, text="INSCRIPTION", bg="white", fg="black", font=("Arial", 12, "bold"),
          command=lambda: afficher_frame(frame_inscription)).pack(pady=10)

tk.Button(frame_accueil, text="SE CONNECTER", bg="white", fg="black", font=("Arial", 12, "bold"),
          command=lambda: afficher_frame(frame_connexion)).pack(pady=10)

# -------------------
# Frames inscription et connexion
# -------------------
frame_inscription = inscription.creer_inscription(root, retour=frame_accueil)
frame_connexion = connection.connexion_utilisateur(root, retour=frame_accueil)

# -------------------
# Afficher la page d'accueil au démarrage
# -------------------
afficher_frame(frame_accueil)

# -------------------
# Lancer la boucle
# -------------------
root.mainloop()
