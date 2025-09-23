import tkinter as tk
import os

def creer_accueil_utilisateur(root, retour=None):
    frame = tk.Frame(root, bg="black")
    tk.Label(frame, text="Bienvenue utilisateur", font=("Arial", 24), bg="black", fg="white").pack(pady=50)
    if retour:
        tk.Button(frame, text="Déconnexion", command=lambda: retour.pack(fill="both", expand=True)).pack(pady=20)
    return frame
