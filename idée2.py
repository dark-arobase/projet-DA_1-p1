import tkinter as tk

# Créer la fenêtre principale
root = tk.Tk()
root.title("Yuppiquiz - Admin")
root.geometry("800x600")
root.configure(bg="white")

# --------------------
# Styles
# --------------------
nav_font = ("Arial", 10, "bold")
button_font = ("Arial", 10, "bold")
main_button_font = ("Arial", 11, "bold")

# --------------------
# Barre de navigation
# --------------------
nav_frame = tk.Frame(root, bg="white")
nav_frame.pack(fill="x", pady=10)

# Boutons de navigation
btn_accueil = tk.Button(nav_frame, text="Accueil", bg="black", fg="white", font=nav_font, padx=10, pady=5)
btn_accueil.pack(side="left", padx=10)

btn_explorer = tk.Button(nav_frame, text="Explorer", bg="black", fg="white", font=nav_font, padx=10, pady=5)
btn_explorer.pack(side="left", padx=10)

btn_mode_utilisateur = tk.Button(nav_frame, text="Mode utilisateur", bg="black", fg="white", font=nav_font, padx=10, pady=5)
btn_mode_utilisateur.pack(side="left", padx=10)

# Nom utilisateur à droite
user_label = tk.Label(nav_frame, text="Nom utilisateur (admin)", font=nav_font, bg="white", fg="black")
user_label.pack(side="right", padx=5)

# Placeholder pour une icône (ex: image ronde)
user_icon = tk.Label(nav_frame, text="👤", font=("Arial", 12))
user_icon.pack(side="right", padx=5)

# --------------------
# Séparateur (ligne noire)
# --------------------
separator = tk.Frame(root, bg="black", height=2)
separator.pack(fill="x", padx=5, pady=5)

# --------------------
# Zone centrale avec les 4 boutons
# --------------------
center_frame = tk.Frame(root, bg="white")
center_frame.pack(pady=50)

# Ligne 1 : Créer + Modifier
btn_creer = tk.Button(center_frame, text="Créé votre quiz", bg="black", fg="white", font=main_button_font, padx=20, pady=10)
btn_creer.grid(row=0, column=0, padx=30, pady=20)

btn_modifier = tk.Button(center_frame, text="Modification d’un\nquiz", bg="black", fg="white", font=main_button_font, padx=20, pady=10)
btn_modifier.grid(row=0, column=1, padx=30, pady=20)

# Ligne 2 : Explorer + Hoster
btn_explorer_quiz = tk.Button(center_frame, text="Explorer d’autre quiz", bg="black", fg="white", font=main_button_font, padx=20, pady=10)
btn_explorer_quiz.grid(row=1, column=0, padx=30, pady=20)

btn_hoster = tk.Button(center_frame, text="Hoster votre quiz", bg="black", fg="white", font=main_button_font, padx=20, pady=10)
btn_hoster.grid(row=1, column=1, padx=30, pady=20)

# --------------------
# Lancer l'application
# --------------------
root.mainloop()
