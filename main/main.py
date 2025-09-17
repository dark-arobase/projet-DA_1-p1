import tkinter as tk
from tkinter import ttk

# Fenêtre principale
root = tk.Tk()
root.title("Yuppiquiz")
root.geometry("500x500")
root.configure(bg="black")


# ----------------------
# Styles personnalisés
# ----------------------
header_font = ("Arial", 24, "bold")
button_font = ("Arial", 10, "bold")
box_title_font = ("Arial", 12, "bold")
box_text_font = ("Arial", 10)


def ouvrir_inscription():
    root.withdraw()  # Cache la fenêtre principale, mais ne la détruit pas

    # Création de la nouvelle fenêtre
    root2 = tk.Toplevel()
    root2.title("INSCRIPTION")
    root2.geometry("800x600")
    root2.configure(bg="white")

    label = tk.Label(root2, text="PAGE INSCRIPTION", font=header_font, bg="white")
    label.pack(pady=40)

    label1 = tk.Label(root2, text="test test")
    

    commentaire = tk.Entry(root2,)
    label1.pack(pady=1)
    commentaire.pack(pady=40)

    def revenir_accueil():
        root2.destroy()     # Ferme la fenêtre d'inscription
        root.deiconify()    # Ré-affiche la fenêtre principale

    
    bt_envoyer = tk.Button(root2, text="Inscription", bg="black", fg="white", font=button_font)
    bt_envoyer.pack(pady=10)

    bt_retour = tk.Button(root2, text="Retour", command=revenir_accueil, bg="black", fg="white", font=button_font)
    bt_retour.pack(pady=20)

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
    bt_retour.pack(pady=20)


# ----------------------
# En-tête (YUPPIQUIZ)
# ----------------------
header_line = tk.Label(root, text="BIENVENUE", bg="black", fg="white", font=header_font)
header_line.place(relx=0.5, rely=0.05, anchor="center")
# ----------------------#
# AU CENTRE #
# ----------------------#
header = tk.Label(root, text="YUPPIQUIZ", bg="black", fg="white", font=header_font)
header.place(relx=0.5, rely=0.3, anchor="center")

# ----------------------
# Boutons haut : Inscription et Connexion
# ----------------------
btn_inscription = tk.Button(root, text="INSCRIPTION", bg="black", fg="white", font=button_font, padx=10, pady=5, command=ouvrir_inscription)
btn_inscription.place(relx=0.01, y=20)

btn_connexion = tk.Button(root, text="SE CONNECTER", bg="black", fg="white", font=button_font, padx=10, pady=5, command=ouvrir_connexion)
btn_connexion.place(relx=0.92, y=20)

# ----------------------
# Boucle principale
# ----------------------
root.mainloop()
