import tkinter as tk
from tkinter import ttk
import csv

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

def ouvrir_un_quiz():
    root.withdraw()  # Cache la fenêtre principale, mais ne la détruit pas

    # Création de la nouvelle fenêtre
    root2 = tk.Toplevel()
    root2.title("Quiz")
    root2.geometry("800x600")
    root2.configure(bg="white")

    label = tk.Label(root2, text=" VEUILLEZ REJOINDRE UN QUIZ", font=header_font, bg="white", fg="white", background="black")
    label.pack(pady=40)

    label1 = tk.Label(root2, text="Entrez le code du quiz :", font=box_text_font, bg="white")
    label1.pack(pady=10)

    code_entry = tk.Entry(root2, font=box_text_font)
    code_entry.pack(pady=10)

    def revenir_accueil():
        root2.destroy()     # Ferme la fenêtre du quiz
        root.deiconify()    # Ré-affiche la fenêtre principale

    bt_rejoindre = tk.Button(root2, text="Rejoindre", bg="black", fg="white", font=button_font)
    bt_rejoindre.pack(pady=10)

    bt_retour = tk.Button(root2, text="Retour", command=revenir_accueil, bg="black", fg="white", font=button_font)
    bt_retour.pack(pady=20)



def ouvrir_inscription():
    root.withdraw()  # Cache la fenêtre principale, mais ne la détruit pas

    # Création de la nouvelle fenêtre
    root3 = tk.Toplevel()
    root3.title("INSCRIPTION")
    root3.geometry("800x600")
    root3.configure(bg="white")

    label = tk.Label(root3, text="PAGE INSCRIPTION", font=header_font, bg="white")
    label.pack(pady=40)
    

    # Frame pour le champ Nom
    frame_nom = tk.Frame(root3, bg="white")
    frame_nom.pack(pady=10)
    label_nom = tk.Label(frame_nom, text="Nom :", font=box_text_font, bg="white")
    label_nom.pack(side="left", padx=(0, 10))
    commentaire = tk.Entry(frame_nom, font=box_text_font)
    commentaire.pack(side="left")

    # Frame pour le champ Mot de passe
    frame_mdp = tk.Frame(root3, bg="white")
    frame_mdp.pack(pady=10)
    label_nom2 = tk.Label(frame_mdp, text="Nouveau mot de passe :", font=box_text_font, bg="white")
    label_nom2.pack(side="left", padx=(0, 10))
    nmdp = tk.Entry(frame_mdp, font=box_text_font, show="*")
    nmdp.pack(side="left")

    # Frame pour le champ Confirmation mot de passe
    frame_rmdp = tk.Frame(root3, bg="white")
    frame_rmdp.pack(pady=10)
    label_nom3 = tk.Label(frame_rmdp, text="Retaper le mot de passe :", font=box_text_font, bg="white")
    label_nom3.pack(side="left", padx=(0, 10))
    rmdp = tk.Entry(frame_rmdp, font=box_text_font, show="*")
    rmdp.pack(side="left")

    # Label pour afficher les messages d'erreur ou de succès
    label_message = tk.Label(root3, text="", font=box_text_font, fg="red", bg="white")
    label_message.pack(pady=5)

    def revenir_accueil():
        root3.destroy()     # Ferme la fenêtre d'inscription
        root.deiconify()    # Ré-affiche la fenêtre principale

    def enrigistedonner():
        #Récupere les information de l'utilisateur
        nom = commentaire.get()  
        mdp = nmdp.get()         
        remdp = rmdp.get()       
        if nom.strip() and mdp.strip() and remdp.strip():  # Vérifie que tous les champs sont remplis
            if mdp == remdp:  # Vérifie que les deux mots de passe sont identiques
                with open("BasedeDonnee.csv", "a", newline="", encoding="utf-8") as f:
                    writer = csv.writer(f)
                    writer.writerow([nom, mdp])  # Enregistre les trois valeurs

                #Vide les case aprés l'ajout des compte
                commentaire.delete(0, tk.END)  
                nmdp.delete(0, tk.END)         
                rmdp.delete(0, tk.END)         
                label_message.config(text="Inscription réussie !", fg="green")
            else:
                label_message.config(text="Les mots de passe ne correspondent pas.", fg="red")
        else:
            label_message.config(text="Veuillez remplir tous les champs.", fg="red")
    

    bt_envoyer = tk.Button(root3, text="Inscription", bg="black", fg="white", font=button_font, command=enrigistedonner)
    bt_envoyer.pack(pady=10)

    bt_retour = tk.Button(root3, text="Retour", command=revenir_accueil, bg="black", fg="white", font=button_font)
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
btn_quiz = tk.Button(root, text="REJOINDRE\nUN QUIZ", bg="black", fg="white", font=button_font, padx=20, pady=10, command=ouvrir_un_quiz)
btn_quiz.place(relx=0.5, rely=0.7, anchor="center")

# ----------------------
# Boucle principale
# ----------------------
root.mainloop()
