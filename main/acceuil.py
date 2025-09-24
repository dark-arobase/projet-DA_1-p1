import tkinter as tk

def creer_accueil_utilisateur(root, retour=None):
    frame = tk.Frame(root, bg="white")

    # ------------------------------
    # BARRE DE NAVIGATION EN HAUT
    # ------------------------------
    navbar = tk.Frame(frame, bg="black", height=50)
    navbar.pack(fill="x")

    # Boutons de navigation (non fonctionnels ici)
    def on_nav_click(name):
        print(f"Navigation : {name}")

    nav_buttons = ["Accueil", "Explorer", "Mode utilisateur"]
    for text in nav_buttons:
        btn = tk.Button(navbar, text=text, command=lambda t=text: on_nav_click(t),
                        bg="black", fg="white", relief="flat", padx=20, pady=10)
        btn.pack(side="left", padx=5, pady=5)

    # Espace utilisateur à droite
    user_frame = tk.Frame(navbar, bg="black")
    user_frame.pack(side="right", padx=10)

    user_label = tk.Label(user_frame, text="", fg="white", bg="black")
    user_label.pack(side="left", padx=5)

    avatar = tk.Canvas(user_frame, width=30, height=30, bg="black", highlightthickness=0)
    avatar.create_oval(5, 5, 25, 25, fill="gray")
    avatar.pack(side="left")

    # ------------------------------
    # MESSAGE D’ACCUEIL
    # ------------------------------
    label = tk.Label(frame, text="Bienvenue sur Yuppiquiz!", font=("Arial", 24, "bold"), fg="blue", bg="white")
    label.pack(pady=20)

    # ------------------------------
    # CONTENU PRINCIPAL (BOUTONS)
    # ------------------------------
    main_frame = tk.Frame(frame, bg="black")
    main_frame.pack(expand=True)

    def on_main_button_click(name):
        print(f"Action : {name}")

    actions = [
        ("Créé votre quiz", 0, 0),
        ("Modification d’un quiz", 0, 1),
        ("Explorer d’autre quiz", 1, 0),
        ("Hoster votre quiz", 1, 1)
    ]

    for text, row, col in actions:
        btn = tk.Button(main_frame, text=text, command=lambda t=text: on_main_button_click(t),
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
                  bg="red", fg="white", font=("Arial", 12, "bold")).pack(pady=20)

    return frame
