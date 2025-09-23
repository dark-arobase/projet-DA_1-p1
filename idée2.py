import tkinter as tk


def ouvrir_admin():
    root = tk.Toplevel()
    root.title("Yuppiquiz - Admin")
    root.geometry("800x600")
    root.configure(bg="white")

    # Styles
    nav_font = ("Arial", 10, "bold")
    button_font = ("Arial", 10, "bold")
    main_button_font = ("Arial", 11, "bold")
    header_font = ("Arial", 24, "bold")
    box_title_font = ("Arial", 12, "bold")
    box_text_font = ("Arial", 10)

    # Barre de navigation
    nav_frame = tk.Frame(root, bg="white")
    nav_frame.pack(fill="x", pady=10)

    btn_accueil = tk.Button(nav_frame, text="Accueil", bg="black", fg="white", font=nav_font, padx=10, pady=5)
    btn_accueil.pack(side="left", padx=10)

    btn_explorer = tk.Button(nav_frame, text="Explorer", bg="black", fg="white", font=nav_font, padx=10, pady=5)
    btn_explorer.pack(side="left", padx=10)

    btn_mode_utilisateur = tk.Button(nav_frame, text="Mode utilisateur", bg="black", fg="white", font=nav_font, padx=10, pady=5)
    btn_mode_utilisateur.pack(side="left", padx=10)

    user_label = tk.Label(nav_frame, text="Nom utilisateur (admin)", font=nav_font, bg="white", fg="black")
    user_label.pack(side="right", padx=5)

    user_icon = tk.Label(nav_frame, text="👤", font=("Arial", 12))
    user_icon.pack(side="right", padx=5)

    separator = tk.Frame(root, bg="black", height=2)
    separator.pack(fill="x", padx=5, pady=5)

    center_frame = tk.Frame(root, bg="white")
    center_frame.pack(pady=50)

    btn_creer = tk.Button(center_frame, text="Créé votre quiz", bg="black", fg="white", font=main_button_font, padx=20, pady=10)
    btn_creer.grid(row=0, column=0, padx=30, pady=20)

    btn_modifier = tk.Button(center_frame, text="Modification d’un\nquiz", bg="black", fg="white", font=main_button_font, padx=20, pady=10)
    btn_modifier.grid(row=0, column=1, padx=30, pady=20)

    def explorer__quiz():
        root.withdraw()
        root2 = tk.Toplevel()
        root2.title("Quiz")
        root2.geometry("800x600")
        root2.configure(bg="black")

        label = tk.Label(root2, text=" VEUILLEZ REJOINDRE UN QUIZ", font=header_font, bg="black", fg="white")
        label.pack(pady=40)

        label1 = tk.Label(root2, text="Entrez le code du quiz :", font=box_text_font, bg="black", fg="white")
        label1.pack(pady=10)

        def revenir_accueil():
            root2.destroy()
            root.deiconify()

        bt_rejoindre = tk.Button(root2, text="Rejoindre", bg="black", fg="white", font=button_font)
        bt_rejoindre.pack(pady=10)
        bt_retour = tk.Button(root2, text="Retour", command=revenir_accueil, bg="black", fg="white", font=button_font)
        bt_retour.pack(pady=20)

    btn_explorer_quiz = tk.Button(center_frame, text="Explorer d’autre quiz", bg="black", fg="white", font=main_button_font, padx=20, pady=10, command=explorer__quiz)
    btn_explorer_quiz.grid(row=1, column=0, padx=30, pady=20)

    btn_hoster = tk.Button(center_frame, text="Hoster votre quiz", bg="black", fg="white", font=main_button_font, padx=20, pady=10)
    btn_hoster.grid(row=1, column=1, padx=30, pady=20)
