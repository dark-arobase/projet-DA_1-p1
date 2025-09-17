import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os
import random

# ----------------------------
# Gestion des données (JSON)
# ----------------------------
def charger_donnees(fichier):
    if os.path.exists(fichier):
        with open(fichier, "r") as f:
            return json.load(f)
    return {}

def sauvegarder_donnees(fichier, data):
    with open(fichier, "w") as f:
        json.dump(data, f, indent=4)

USERS_FILE = "data/users.json"
QUIZZES_FILE = "data/quizzes.json"
SCORES_FILE = "data/scores.json"

# ----------------------------
# Classes
# ----------------------------
class Utilisateur:
    def __init__(self, nom, email, mot_de_passe, role="joueur"):
        self.nom = nom
        self.email = email
        self.mot_de_passe = mot_de_passe
        self.role = role

class Quiz:
    def __init__(self, titre, createur):
        self.id = str(random.randint(1000, 9999))  # code PIN unique
        self.titre = titre
        self.createur = createur
        self.questions = []

    def ajouter_question(self, texte, reponses, bonne):
        self.questions.append({
            "texte": texte,
            "reponses": reponses,
            "bonne": bonne
        })

# ----------------------------
# Interface Tkinter
# ----------------------------
class YuppiQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("YuppiQuiz")
        self.utilisateur = None
        self.show_login()

    # --- Pages ---
    def show_login(self):
        self.clear()
        tk.Label(self.root, text="Connexion", font=("Arial", 18)).pack(pady=10)

        tk.Label(self.root, text="Email").pack()
        email = tk.Entry(self.root)
        email.pack()

        tk.Label(self.root, text="Mot de passe").pack()
        mdp = tk.Entry(self.root, show="*")
        mdp.pack()

        def login_action():
            users = charger_donnees(USERS_FILE)
            if email.get() in users and users[email.get()]["mot_de_passe"] == mdp.get():
                self.utilisateur = users[email.get()]
                messagebox.showinfo("Succès", f"Bienvenue {self.utilisateur['nom']} !")
                self.show_menu()
            else:
                messagebox.showerror("Erreur", "Identifiants invalides")

        tk.Button(self.root, text="Se connecter", command=login_action).pack(pady=5)
        tk.Button(self.root, text="Inscription", command=self.show_register).pack()

    def show_register(self):
        self.clear()
        tk.Label(self.root, text="Inscription", font=("Arial", 18)).pack(pady=10)

        tk.Label(self.root, text="Nom").pack()
        nom = tk.Entry(self.root)
        nom.pack()

        tk.Label(self.root, text="Email").pack()
        email = tk.Entry(self.root)
        email.pack()

        tk.Label(self.root, text="Mot de passe").pack()
        mdp = tk.Entry(self.root, show="*")
        mdp.pack()

        role = tk.StringVar(value="joueur")
        tk.Radiobutton(self.root, text="Joueur", variable=role, value="joueur").pack()
        tk.Radiobutton(self.root, text="Créateur", variable=role, value="createur").pack()

        def register_action():
            users = charger_donnees(USERS_FILE)
            if email.get() in users:
                messagebox.showerror("Erreur", "Email déjà utilisé")
            else:
                users[email.get()] = {
                    "nom": nom.get(),
                    "mot_de_passe": mdp.get(),
                    "role": role.get()
                }
                sauvegarder_donnees(USERS_FILE, users)
                messagebox.showinfo("Succès", "Compte créé avec succès !")
                self.show_login()

        tk.Button(self.root, text="S'inscrire", command=register_action).pack(pady=5)
        tk.Button(self.root, text="Retour", command=self.show_login).pack()

    def show_menu(self):
        self.clear()
        tk.Label(self.root, text=f"Bienvenue {self.utilisateur['nom']} ({self.utilisateur['role']})", font=("Arial", 16)).pack(pady=10)

        if self.utilisateur["role"] == "createur":
            tk.Button(self.root, text="Créer un quiz", command=self.creer_quiz).pack(pady=5)

        tk.Button(self.root, text="Rejoindre un quiz", command=self.rejoindre_quiz).pack(pady=5)
        tk.Button(self.root, text="Déconnexion", command=self.show_login).pack(pady=10)

    def creer_quiz(self):
        titre = simpledialog.askstring("Création quiz", "Titre du quiz :")
        if not titre: return
        quiz = Quiz(titre, self.utilisateur["nom"])

        while True:
            q = simpledialog.askstring("Nouvelle question", "Écris la question (ou laisse vide pour finir):")
            if not q: break
            r1 = simpledialog.askstring("Réponse", "Réponse 1 :")
            r2 = simpledialog.askstring("Réponse", "Réponse 2 :")
            r3 = simpledialog.askstring("Réponse", "Réponse 3 :")
            r4 = simpledialog.askstring("Réponse", "Réponse 4 :")
            bonne = simpledialog.askstring("Bonne réponse", "Quelle est la bonne réponse ?")

            quiz.ajouter_question(q, [r1, r2, r3, r4], bonne)

        quizzes = charger_donnees(QUIZZES_FILE)
        quizzes[quiz.id] = {
            "titre": quiz.titre,
            "createur": quiz.createur,
            "questions": quiz.questions
        }
        sauvegarder_donnees(QUIZZES_FILE, quizzes)
        messagebox.showinfo("Succès", f"Quiz créé avec code PIN : {quiz.id}")

    def rejoindre_quiz(self):
        code = simpledialog.askstring("Rejoindre quiz", "Entre le code PIN :")
        quizzes = charger_donnees(QUIZZES_FILE)
        if code not in quizzes:
            messagebox.showerror("Erreur", "Quiz introuvable")
            return
        quiz = quizzes[code]
        score = 0
        for q in quiz["questions"]:
            rep = simpledialog.askstring("Question", f"{q['texte']}\n{q['reponses']}")
            if rep == q["bonne"]:
                score += 1
        messagebox.showinfo("Résultat", f"Score final : {score}/{len(quiz['questions'])}")

    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# ----------------------------
# Lancement
# ----------------------------
if __name__ == "__main__":
    os.makedirs("data", exist_ok=True)
    root = tk.Tk()
    app = YuppiQuizApp(root)
    root.mainloop()
