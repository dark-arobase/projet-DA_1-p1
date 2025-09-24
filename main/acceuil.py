import tkinter as tk

import explore_quiz
import crée_quiz 
import modification_quiz

def creer_accueil_utilisateur(root, nom, retour=None):
    frame = tk.Frame(root, bg="white")

    # ------------------------------
    # BARRE DE NAVIGATION EN HAUT
    # ------------------------------
    navbar = tk.Frame(frame, bg="black", height=50)
    navbar.pack(fill="x")

    def on_nav_click(name):
        print(f"Navigation : {name}")

    nav_buttons = ["Accueil", "Explorer", "Mode utilisateur"]
    for text in nav_buttons:
        btn = tk.Button(navbar, text=text, command=lambda t=text: on_nav_click(t),
                        bg="black", fg="white", relief="flat", padx=20, pady=10)
        btn.pack(side="left", padx=5, pady=5)

    # Espace utilisateur à droite
    user_frame = tk.Frame(navbar, bg="gray")
    user_frame.pack(side="right", padx=10)

    user_label = tk.Label(user_frame, text=f"{nom}, (admin)", fg="white", bg="black")
    user_label.pack(side="left", padx=5)

    avatar = tk.Canvas(user_frame, width=30, height=30, bg="black", highlightthickness=0)
    avatar.create_oval(5, 5, 25, 25, fill="gray")
    avatar.pack(side="left")

    # ------------------------------
    # MESSAGE D’ACCUEIL
    # ------------------------------
    label = tk.Label(frame, text="Bienvenue sur Yuppiquiz!", font=("Arial", 24, "bold"), fg="#2B2626")
    label.pack(pady=20)

    # ------------------------------
    # CONTENU PRINCIPAL (BOUTONS)
    # ------------------------------
    main_frame = tk.Frame(frame, bg="black")
    main_frame.pack(expand=True)

    def on_main_button_click(name):
        print(f"Action : {name}")
        if name =="Créé votre quiz":
            


    def open_explorer():
        frame.pack_forget()  # cacher accueil
        quiz_frame = (root, frame)
        quiz_frame.pack(fill="both", expand=True)

    actions = [
        ("Créer votre quiz", 0, 0, lambda: changer_page(frame, crée_quiz.page_cree_quiz(root, nom, retour=frame))),
        ("Modification d’un quiz", 0, 1, lambda: changer_page(frame, modification_quiz.page_modification_quiz(root, nom, retour=frame))),
        ("Explorer d’autre quiz", 1, 0, lambda: changer_page(frame, explore_quiz.page_explorer_quiz(root, nom, retour=frame))),
    ]

    for text, row, col, cmd in actions:
        btn = tk.Button(main_frame, text=text, command=cmd,
                        bg="black", fg="white", font=("Arial", 12, "bold"), width=20, height=3)
        btn.grid(row=row, column=col, padx=40, pady=30)

    main_frame.grid_rowconfigure((0, 1), weight=1)
    main_frame.grid_columnconfigure((0, 1), weight=1)

    # ------------------------------
    # BOUTON DE DECONNEXION
    # ------------------------------
    if retour:
        def deconnexion():
            frame.pack_forget()
            retour.pack(fill="both", expand=True)

        tk.Button(frame, text="Déconnexion", command=deconnexion,
                  bg="black", fg="white", font=("Arial", 12, "bold")).pack(pady=20)

    return frame

#-------
def changer_page(frame_actuel, frame_suivant):
    frame_actuel.pack_forget()
    frame_suivant.pack(fill="both", expand=True)
#-------

# Mode test autonome
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Test - Accueil Utilisateur")
    root.geometry("800x600")
    root.configure(bg="black")

    frame_test = creer_accueil_utilisateur(root, nom="TOTO")
    frame_test.pack(fill="both", expand=True)

    root.mainloop()


'''
import tkinter as tk
import explore_quiz
import cree_quiz
import modification_quiz

def creer_accueil_utilisateur(root, nom, retour=None):
    frame = tk.Frame(root, bg="white")

    # Barre de navigation simplifiée
    navbar = tk.Frame(frame, bg="black", height=50)
    navbar.pack(fill="x")

    nav_buttons = ["Accueil", "Explorer", "Mode utilisateur"]
    for text in nav_buttons:
        btn = tk.Button(navbar, text=text, bg="black", fg="white", relief="flat", padx=20, pady=10)
        btn.pack(side="left", padx=5, pady=5)

    # Label bienvenue
    label = tk.Label(frame, text=f"Bienvenue {nom} sur Yuppiquiz!", font=("Arial", 24, "bold"), fg="#2B2626", bg="white")
    label.pack(pady=20)

    # Contenu principal avec boutons
    main_frame = tk.Frame(frame, bg="black")
    main_frame.pack(expand=True)

    def open_cree_quiz():
        changer_page(frame, cree_quiz.page_cree_quiz(root, nom, retour=frame))

    def open_modif_quiz():
        changer_page(frame, modification_quiz.page_modification_quiz(root, nom, retour=frame))

    def open_explorer():
        changer_page(frame, explore_quiz.page_explorer_quiz(root, nom, retour=frame))

    actions = [
        ("Créer votre quiz", 0, 0, open_cree_quiz),
        ("Modification d’un quiz", 0, 1, open_modif_quiz),
        ("Explorer d’autre quiz", 1, 0, open_explorer),
    ]

    for text, row, col, cmd in actions:
        btn = tk.Button(main_frame, text=text, command=cmd,
                        bg="black", fg="white", font=("Arial", 12, "bold"),
                        width=20, height=3)
        btn.grid(row=row, column=col, padx=40, pady=30)

    main_frame.grid_rowconfigure((0, 1), weight=1)
    main_frame.grid_columnconfigure((0, 1), weight=1)

    # Bouton déconnexion
    if retour:
        def deconnexion():
            frame.pack_forget()
            retour.pack(fill="both", expand=True)

        tk.Button(frame, text="Déconnexion", command=deconnexion,
                  bg="black", fg="white", font=("Arial", 12, "bold")).pack(pady=20)

    return frame

def changer_page(frame_actuel, frame_suivant):
    frame_actuel.pack_forget()
    frame_suivant.pack(fill="both", expand=True)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Yuppiquiz - Accueil Utilisateur")
    root.geometry("800x600")
    root.configure(bg="white")

    frame_accueil = creer_accueil_utilisateur(root, nom="TOTO")
    frame_accueil.pack(fill="both", expand=True)

    root.mainloop()
'''
