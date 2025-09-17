import tkinter as tk
from tkinter import ttk

# Fenêtre principale
root = tk.Tk()
root.title("Yuppiquiz")
root.geometry("800x600")
root.configure(bg="white")

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

    commentaire = tk.Entry(root2)
    commentaire.pack(pady=40)

    def revenir_accueil():
        root2.destroy()     # Ferme la fenêtre d'inscription
        root.deiconify()    # Ré-affiche la fenêtre principale

    bt_retour = tk.Button(root2, text="RETOUR", command=revenir_accueil, bg="black", fg="white", font=button_font)
    bt_retour.pack(pady=20)

# ----------------------
# En-tête (YUPPIQUIZ)
# ----------------------
header = tk.Label(root, text="YUPPIQUIZ", bg="black", fg="white", font=header_font, padx=20, pady=10)
header.place(relx=0.5, rely=0.05, anchor="n")

# ----------------------
# Boutons haut : Inscription et Connexion
# ----------------------
btn_inscription = tk.Button(root, text="INSCRIPTION", bg="black", fg="white", font=button_font, padx=10, pady=5, command=ouvrir_inscription)
btn_inscription.place(x=20, y=20)

btn_connexion = tk.Button(root, text="SE CONNECTER", bg="black", fg="white", font=button_font, padx=10, pady=5)
btn_connexion.place(relx=1.0, x=-140, y=20, anchor="ne")

# ----------------------
# Cadre Apprentissage
# ----------------------
frame_apprentissage = tk.Frame(root, highlightbackground="black", highlightthickness=1)
frame_apprentissage.place(relx=0.2, rely=0.3, anchor="n", width=250, height=150)

label_apprentissage_title = tk.Label(frame_apprentissage, text="APPRENTISSAGE", bg="black", fg="white", font=box_title_font)
label_apprentissage_title.pack(fill="x")

label_apprentissage_text = tk.Label(frame_apprentissage, text="Ici on parle des information ou\nétudes supplémentaire l’étudiant\npeut apprendre.", font=box_text_font, justify="left", pady=10)
label_apprentissage_text.pack()

# ----------------------
# Cadre Matière
# ----------------------
frame_matiere = tk.Frame(root, highlightbackground="black", highlightthickness=1)
frame_matiere.place(relx=0.7, rely=0.3, anchor="n", width=250, height=150)

label_matiere_title = tk.Label(frame_matiere, text="MATIÈRE", bg="black", fg="white", font=box_title_font)
label_matiere_title.pack(fill="x")

label_matiere_list = tk.Label(
    frame_matiere,
    text="• Math\n• Français\n• Anglais\n• Physique\n• etc.",
    font=box_text_font,
    justify="left",
    pady=10
)
label_matiere_list.pack()

# ----------------------
# Bouton Rejoindre un Quiz
# ----------------------
btn_quiz = tk.Button(root, text="REJOINDRE\nUN QUIZ", bg="black", fg="white", font=button_font, padx=20, pady=10)
btn_quiz.place(relx=0.5, rely=0.7, anchor="center")

# ----------------------
# Boucle principale
# ----------------------
root.mainloop()
