import json
import interface_jeu
import tkinter as tk

def page_explorer_quiz(root, nom=None, retour=None):
    frame = tk.Frame(root, bg="black")
    root.title("Explorer Quiz")
    frame.pack(fill="both", expand=True)

    # Barre du haut
    navbar = tk.Frame(frame, bg="black", height=50)
    navbar.pack(fill="x")
    user_frame = tk.Frame(navbar, bg="black")
    user_frame.pack(side="right", padx=10)
    user_label = tk.Label(user_frame, text=f"{nom}", fg="white", bg="black")
    user_label.pack(side="left", padx=5)
    title = tk.Label(frame, text="Page Explorer Quiz", font=("Arial", 20, "bold"), fg="white", bg="black")
    title.pack(pady=20)

    # Recherche
    search_frame = tk.Frame(frame, bg="black")
    search_frame.pack(pady=10)
    tk.Label(search_frame, text="Rechercher :", font=("Arial", 24, "bold"), bg="black", fg="white").pack(side="left")
    entry_search = tk.Entry(search_frame, font=("Arial", 24, "bold"), bg="black", fg="white")
    entry_search.pack(side="left", padx=5)
    btn_search = tk.Button(search_frame, text="🔍", font=("Arial", 24, "bold"), bg="black", fg="white")
    btn_search.pack(side="left", padx=5)

    
    # Zone des quiz
    grid_frame = tk.Frame(frame, bg="black")
    grid_frame.pack(expand=True, pady=20)

    try:
        with open("main/data/quiz.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        tk.Label(grid_frame, text="Fichier quiz.json introuvable", fg="red", bg="black").pack(pady=20)
        return frame

    def changer_page(frame_actuel, frame_suivant):
        frame_actuel.pack_forget()
        frame_suivant.pack(fill="both", expand=True)

    def afficher_quizzes(filtre=""):
        # vide les anciens
        for widget in grid_frame.winfo_children():
            widget.destroy()

        cols = 5
        for i, quiz in enumerate(data):
            titre = quiz.get("titre", "")
            if filtre.lower() in titre.lower():
                row = i // cols
                col = i % cols
                btn = tk.Button(
                    grid_frame,
                    text=titre,
                    font=("Arial", 16, "bold"),
                    bg="black",
                    fg="white",
                    width=20,
                    height=3,
                    relief="raised",
                    bd=3,
                    command=lambda t=titre: changer_page(
                        frame,
                        interface_jeu.page_joueur(root, nom, retour=frame, texte=t)
                    )
                )
                btn.grid(row=row, column=col, padx=20, pady=15)

    def do_search():
        clé = entry_search.get().strip()
        afficher_quizzes(clé)

    btn_search.config(command=do_search)

    # Affiche tout de base
    afficher_quizzes()

    # Bouton retour
    def retour_accueil():
        frame.pack_forget()
        if retour:
            retour.pack(fill="both", expand=True)

    btn_retour = tk.Button(frame, text="Retour",
                           command=retour_accueil,
                           font=("Arial", 14, "bold"),
                           bg="black", fg="white", width=10)
    btn_retour.pack(pady=10)

    return frame


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Explorer Quiz")
    root.geometry("900x600")
    root.configure(bg="black")

    frm = page_explorer_quiz(root, nom="")
    frm.pack(fill="both", expand=True)
    root.mainloop()
