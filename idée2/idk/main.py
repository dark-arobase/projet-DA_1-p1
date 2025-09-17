import tkinter as tk
from tkinter import messagebox

# ----------------------------
# Classes (POO)
# ----------------------------
class Utilisateur:
    def __init__(self, id, nom, email, mot_de_passe):
        self.id = id
        self.nom = nom
        self.email = email
        self.mot_de_passe = mot_de_passe

class Joueur(Utilisateur):
    def __init__(self, id, nom, email, mot_de_passe):
        super().__init__(id, nom, email, mot_de_passe)
        self.scores = []

    def ajouter_score(self, score):
        self.scores.append(score)

class Createur(Utilisateur):
    def __init__(self, id, nom, email, mot_de_passe):
        super().__init__(id, nom, email, mot_de_passe)
        self.quiz_crees = []

    def creer_quiz(self, titre):
        quiz = Quiz(len(self.quiz_crees) + 1, titre)
        self.quiz_crees.append(quiz)
        return quiz

class Quiz:
    def __init__(self, id, titre):
        self.id = id
        self.titre = titre
        self.questions = []

    def ajouter_question(self, question):
        self.questions.append(question)

class Question:
    def __init__(self, texte, reponses, bonne_reponse):
        self.texte = texte
        self.reponses = reponses  # liste de Réponse
        self.bonne_reponse = bonne_reponse

    def est_correcte(self, choix):
        return choix == self.bonne_reponse

class Reponse:
    def __init__(self, texte):
        self.texte = texte

class Score:
    def __init__(self, points=0):
        self.points = points

# ----------------------------
# Interface Tkinter
# ----------------------------
class YuppiQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("YuppiQuiz")

        # Exemple de quiz
        self.quiz = Quiz(1, "Culture générale")
        self.quiz.ajouter_question(
            Question("Capital de la France ?", ["Paris", "Londres", "Rome", "Berlin"], "Paris")
        )
        self.quiz.ajouter_question(
            Question("2 + 2 = ?", ["3", "4", "5", "6"], "4")
        )

        self.score = Score()
        self.index_q = 0

        # Interface principale
        self.label = tk.Label(root, text="Bienvenue sur YuppiQuiz !", font=("Arial", 16))
        self.label.pack(pady=10)

        self.start_button = tk.Button(root, text="Commencer le quiz", command=self.lancer_quiz)
        self.start_button.pack(pady=10)

    def lancer_quiz(self):
        self.afficher_question()

    def afficher_question(self):
        if self.index_q < len(self.quiz.questions):
            q = self.quiz.questions[self.index_q]

            self.clear_window()
            tk.Label(self.root, text=q.texte, font=("Arial", 14)).pack(pady=10)

            for rep in q.reponses:
                tk.Button(self.root, text=rep, command=lambda r=rep: self.verifier_reponse(r)).pack(pady=5)
        else:
            self.afficher_resultat()

    def verifier_reponse(self, choix):
        q = self.quiz.questions[self.index_q]
        if q.est_correcte(choix):
            self.score.points += 1
        self.index_q += 1
        self.afficher_question()

    def afficher_resultat(self):
        self.clear_window()
        tk.Label(self.root, text=f"Score final : {self.score.points}/{len(self.quiz.questions)}", font=("Arial", 16)).pack(pady=20)
        tk.Button(self.root, text="Quitter", command=self.root.quit).pack()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# ----------------------------
# Lancement de l'application
# ----------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = YuppiQuizApp(root)
    root.mainloop()
