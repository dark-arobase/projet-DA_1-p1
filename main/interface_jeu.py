import tkinter as tk
import explore_quiz
import crée_quiz 
import modification_quiz
import createur
import json


def page_joueur(root, nom=None, retour=None, texte=None):
    frame = tk.Frame(root, bg="white")
    frame.pack(fill="both", expand=True)

    # --- Barre du haut (nom utilisateur)
    navbar = tk.Frame(frame, bg="black", height=10)
    navbar.pack(fill="x")

    user_frame = tk.Frame(navbar, bg="gray")
    user_frame.pack(side="right", padx=10)

    user_label = tk.Label(user_frame, text=f"{nom}, (admin)", fg="white", bg="black")
    user_label.pack(side="left", padx=5)

    tk.Label(frame, text="Zone de Quiz", font=("Arial", 24, "bold"), fg="black", bg="white").pack(pady=20)

    # Charger les quiz
    with open("main/data/quiz.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    # Chercher le quiz correspondant
    quiz = next((q for q in data if q['titre'] == texte), None)
    if not quiz:
        tk.Label(frame, text="❌ Ce quiz n'existe pas", fg="red", bg="white").pack(pady=20)
        return

    questions = quiz["questions"]
    total = len(questions)
    score = [0]  # score dans une liste pour qu'il soit modifiable dans des sous-fonctions
    index_question = [0]  # même logique

    # Widgets dynamiques à mettre à jour
    question_label = tk.Label(frame, text="", font=("Arial", 16), bg="white", wraplength=700)
    question_label.pack(pady=10)

    choix_var = tk.StringVar()
    boutons_radio = []
    feedback_label = tk.Label(frame, text="", font=("Arial", 12, "italic"), bg="white")
    feedback_label.pack(pady=5)

    # Score final (affiché à la fin)
    score_label = tk.Label(frame, text="", font=("Arial", 14), bg="white")

    # Fonction de vérification immédiate
    def verifier_reponse():
        reponse_donnee = choix_var.get()
        bonne_reponse = questions[index_question[0]]["reponse"]

        if reponse_donnee == bonne_reponse:
            feedback_label.config(text="✅ Bonne réponse", fg="green")
            score[0] += 1
        else:
            feedback_label.config(text=f"❌ Mauvaise réponse (bonne réponse : {bonne_reponse})", fg="red")

        # Désactiver tous les boutons radio après réponse
        for rb in boutons_radio:
            rb.config(state="disabled")

        bouton_suivant.config(state="normal")

    # Fonction pour afficher la prochaine question
    def afficher_question():
        feedback_label.config(text="")
        bouton_suivant.config(state="disabled")
        choix_var.set("")

        # Nettoyage des anciens boutons radio
        for rb in boutons_radio:
            rb.destroy()
        boutons_radio.clear()

        q = questions[index_question[0]]
        question_label.config(text=f"Q{index_question[0]+1}: {q['question']}")

        for choix in q["choix"]:
            rb = tk.Radiobutton(frame, text=choix, variable=choix_var, value=choix,
                                command=verifier_reponse, bg="white", anchor="w")
            rb.pack(fill="x", padx=30)
            boutons_radio.append(rb)

    # Fonction quand on clique sur "Suivant"
    def question_suivante():
        index_question[0] += 1
        if index_question[0] < total:
            afficher_question()
        else:
            # Fin du quiz
            question_label.config(text="🎉 Quiz terminé !")
            feedback_label.config(text="")
            for rb in boutons_radio:
                rb.destroy()
            bouton_suivant.pack_forget()
            score_label.config(text=f"✅ Score final : {score[0]} / {total}")
            score_label.pack(pady=20)

            redo=tk.Button(frame, text="Recommencer", fg="white", bg="green", command=afficher_question, width=10)
            redo.pack()

    # Bouton Suivant
    bouton_suivant = tk.Button(frame, text="Suivant", command=question_suivante,
                               font=("Arial", 12), bg="blue", fg="white", state="disabled")
    bouton_suivant.pack(pady=10)


    # Démarrage : afficher la 1ère question
    afficher_question()



    def changer_page(frame_actuel, frame_suivant):
      frame_actuel.pack_forget()
      frame_suivant.pack(fill="both", expand=True)

    def retour_accueil():
        frame.pack_forget()
        if retour:
            retour.pack(fill="both", expand=True)

    btn_retour = tk.Button(frame, text="Retour",
                           command=retour_accueil,
                           font=("Arial", 14, "bold"),
                           bg="red", fg="white", width=10)
    btn_retour.pack(pady=20)



    root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Test - Page Explorer Quiz")
    root.geometry("800x600")
    root.configure(bg="black")

    main_frame = page_joueur(root, None, root, texte="Mathematique")
    main_frame.pack(fill="both", expand=True)

    root.mainloop()