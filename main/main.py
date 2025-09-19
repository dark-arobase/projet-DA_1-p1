import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import connection
import inscription

# Fenêtre principale
root = tk.Tk()
root.title("Yuppiquiz")
root.geometry("500x500")
root.configure(bg="black")

# Charger et afficher une image
img = Image.open("main/img/pattern.png")  # Assure-toi que le chemin est bon)
photo = ImageTk.PhotoImage(img)

img_label = tk.Label(root, image=photo, bg="black")
img_label.image = photo  # Nécessaire pour empêcher le garbage collection
img_label.pack()

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
#---------------------------
'''frame_accueil = tk.Frame(root, bg="black")
connection.frame_accueil = frame_accueil
inscription.frame_accueil = frame_accueil


# Initialise les modules avec la fenêtre root
connection.set_root(root)
inscription.set_root(root)

frame_connexion = connection.creer_connexion()
frame_inscription = inscription.creer_inscription()

# Afficher la page d'accueil par défaut
frame_accueil.pack(fill="both", expand=True)'''

#---------------------------..

# Créer un rectangle (frame) centré
frame = tk.Frame(root, width=320, height=360, bg="black", highlightthickness=2, highlightbackground="white")
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Ajouter une phrase dans le rectangle
label_title = tk.Label(frame, text="Bienvenue sur Yuppiquiz !", bg="black", fg="white", font=("Arial", 14, "bold"))
label_title.pack(pady=(30, 10))

label_desc = tk.Label(frame, text="Testez vos connaissances et amusez-vous.", bg="black", fg="white", font=("Arial", 11))
label_desc.pack(pady=(0, 30))

# Ajouter des boutons dans le rectangle
btn_inscription = tk.Button(frame, text="INSCRIPTION", bg="white", fg="black", font=("Arial", 12, "bold"),command=ouvrir_inscription)
btn_inscription.pack(pady=10)

btn_connexion = tk.Button(frame, text="SE CONNECTER", bg="white", fg="black", font=("Arial", 12, "bold"),command=ouvrir_connexion)
btn_connexion.pack(pady=10)


# Exemple de bouton à l'extérieur du rectangle (frame)
btn_exterieur = tk.Button(root, text="Bouton extérieur", bg="white", fg="black", font=("Arial", 12, "bold"))
btn_exterieur.place(x=0, y=0)  # Position absolue (x, y) dans la fenêtre principale
    

root.mainloop()
