import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import connection
import inscription
# connection.py


def creer_connexion(root, retour_accueil):
    frame = tk.Frame(root, bg="white")

    titre = tk.Label(frame, text="PAGE CONNEXION", font=("Arial", 24, "bold"), bg="white")
    titre.pack(pady=40)

    entry_nom = tk.Entry(frame)
    entry_nom.pack(pady=10)

    bouton_retour = tk.Button(frame, text="Retour", command=lambda: changer_page(frame, retour_accueil), bg="black", fg="white")
    bouton_retour.pack(pady=20)

    return frame

def changer_page(frame_actuel, frame_suivant):
    frame_actuel.pack_forget()
    frame_suivant.pack(fill="both", expand=True)




'''
def ouvrir_connexion():
    root.withdraw() 

    # Création de la nouvelle fenêtre
    root3 = tk.Toplevel()
    root3.title("CONNEXION")
    root3.geometry("800x600")
    root3.configure(bg="white")

    label = tk.Label(root3, text="PAGE CONNEXION", font=header_font, bg="white")
    label.pack(pady=40)

    def revenir_accueil():
        root3.destroy()     
        root.deiconify()    
    bt_retour = tk.Button(root3, text="Retour", command=revenir_accueil, bg="black", fg="white", font=button_font)
    bt_retour.pack(pady=20)'''