import tkinter as tk
import json

def page_joueur(root, nom=None, retour=None, texte=None):
    frame = tk.Frame(root, bg="white")
    root.title("partie quiz")
    frame.pack(fill="both", expand=True)

    # --- Barre du haut (nom utilisateur)
    navbar = tk.Frame(frame, bg="black", height=30)
    navbar.pack(fill="x")

    user_frame = tk.Frame(navbar, bg="black")
    user_frame.pack(side="right", padx=10)

    user_label = tk.Label(user_frame, text=f"{nom}, (admin)", fg="white", bg="black")
    user_label.pack(side="left", padx=5)

    # Titre principal
    tk.Label(frame, text="Zone de Quiz", font=("Arial", 24, "bold"), fg="black", bg="white").pack(pady=20)

    # --- Charger les quiz depuis fichier JSON ---
    try:
        with open("main/data/quiz.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        tk.Label(frame, text="❌ Fichier quiz.json introuvable", fg="red", bg="white").pack(pady=20)
        return frame

    # --- Chercher le quiz correspondant ---
    quiz = next((q for q in data if q['titre'] == texte), None)
    if not quiz:
        tk.Label(frame, text="❌ Ce quiz n'existe pas", fg="red", bg="white").pack(pady=20)
        return frame

    questions = quiz["questions"]
    total = len(questions)
    score = [0]
    index_question = [0]

    # --- Cadre principal pour question et réponses ---
    main_content = tk.Frame(frame, bg="white")
    main_content.pack(fill="both", expand=True)

    question_label = tk.Label(main_content, text="", font=("Arial", 16), bg="white", wraplength=700)
    question_label.pack(pady=10)

    boutons_radio = []
    feedback_label = tk.Label(main_content, text="", font=("Arial", 12, "italic"), bg="white")
    feedback_label.pack(pady=5)

    score_label = tk.Label(main_content, text="", font=("Arial", 14), bg="white")

    # --- Frame du bas pour boutons ---
    bottom_frame = tk.Frame(frame, bg="white")
    bottom_frame.pack(fill="x", side="bottom", pady=20)

    # Bouton Suivant (désactivé au départ)
    bouton_suivant = tk.Button(
        bottom_frame,
        text="Suivant",
        command=lambda: question_suivante(),bg="black", fg="white", font=("Arial",  18, "bold"),width=12,height=2)
    bouton_suivant.pack(side="right", padx=10)

    # Bouton Retour (toujours visible)
    btn_retour = tk.Button(
        bottom_frame,
        text="Retour",
        command=lambda: retour_accueil(),bg="black", fg="white", font=("Arial",  18, "bold"),width=12,height=2)
    btn_retour.pack(side="left", padx=10)

    # --- Fonction verifier la réponse ---
    def verifier_reponse(reponse_donnee):
        bonne_reponse = questions[index_question[0]]["reponse"]

        if reponse_donnee == bonne_reponse:
            feedback_label.config(text="✅ Bonne réponse", fg="green")
            score[0] += 1
        else:
            feedback_label.config(text=f"❌ Mauvaise réponse (bonne réponse : {bonne_reponse})", fg="red")

        # Désactiver les boutons des réponses après sélection
        for btn in boutons_radio:
            btn.config(state="disabled")

        bouton_suivant.config(state="normal")

    # --- Afficher question ---
    def afficher_question():
        feedback_label.config(text="")
        bouton_suivant.config(state="disabled")
        score_label.pack_forget()

        # Supprimer anciens boutons
        for btn in boutons_radio:
            btn.destroy()
        boutons_radio.clear()

        # Supprimer ancienne frame des réponses si elle existe
        if hasattr(afficher_question, "reponses_frame"):
            afficher_question.reponses_frame.destroy()

        afficher_question.reponses_frame = tk.Frame(main_content, bg="white")
        afficher_question.reponses_frame.pack(pady=20)

        q = questions[index_question[0]]
        question_label.config(text=f"Q{index_question[0]+1}: {q['question']}")

        for i, choix in enumerate(q["choix"]):
            row = i // 2
            col = i % 2
            btn = tk.Button(
                afficher_question.reponses_frame,
                text=choix,
                font=("Arial", 12, "bold"),
                bg="black",
                fg="white",
                width=25,
                height=4,
                relief="raised",
                bd=4,
                command=lambda c=choix: verifier_reponse(c)
            )
            btn.grid(row=row, column=col, padx=20, pady=15)
            boutons_radio.append(btn)

    # --- Fonction question suivante ---
    def question_suivante():
        index_question[0] += 1
        if index_question[0] < total:
            afficher_question()
        else:
            # Fin du quiz
            question_label.config(text="🎉 Quiz terminé !")
            feedback_label.config(text="")
            for btn in boutons_radio:
                btn.destroy()
            bouton_suivant.pack_forget()  # cache le bouton Suivant

            # Affiche score
            score_label.config(text=f"✅ Score final : {score[0]} / {total}")
            score_label.pack(pady=20)

            # Bouton Recommencer (placé sous le score)
            redo = tk.Button(main_content,text="Recommencer", bg="black", fg="white", 
                font=("Arial", 12, "bold"),width=12,height=2,command=rejouer)
            redo.pack(pady=10)
            afficher_question.redo_btn = redo  # Pour pouvoir le détruire plus tard

    # --- Fonction rejouer ---
    def rejouer():
        index_question[0] = 0
        score[0] = 0
        score_label.config(text="")
        feedback_label.config(text="")

        # Supprimer le bouton Recommencer
        if hasattr(afficher_question, "redo_btn"):
            afficher_question.redo_btn.destroy()

        # Remettre le bouton Suivant (toujours à droite dans bottom_frame)
        bouton_suivant.pack(side="right", padx=10)
        bouton_suivant.config(state="disabled")

        afficher_question()

    # --- Fonction retour ---
    def retour_accueil():
        # Cacher la frame quiz
        frame.pack_forget()
        # Remettre la frame retour si elle est définie
        if retour:
            retour.pack(fill="both", expand=True)
        else:
            print("Pas de frame de retour définie")

    # --- Lancement ---
    afficher_question()

    return frame

# Pour test direct si ce fichier est lancé
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Test - Page Joueur")
    root.geometry("800x600")
    root.configure(bg="white")

    frame_test = page_joueur(root, nom="Admin", retour=None, texte="Mathematics")
    frame_test.pack(fill="both", expand=True)

    root.mainloop()
