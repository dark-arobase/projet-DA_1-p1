
# app.py
import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import time, random

from models.utilisateur import Utilisateur
from models.quiz import Quiz, Question, Score
import storage

class YuppiQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("YuppiQuiz")
        self.users = storage.load_users()
        self.quizzes = storage.load_quizzes()
        self.scores = storage.load_scores()  # dict
        self.current_user = None
        self.build_login()

    def build_login(self):
        self.clear()
        tk.Label(self.root, text="YuppiQuiz — Connexion", font=("Arial", 18)).pack(pady=10)

        frame = tk.Frame(self.root)
        frame.pack(pady=5)
        tk.Label(frame, text="Email").grid(row=0, column=0)
        email_entry = tk.Entry(frame)
        email_entry.grid(row=0, column=1)
        tk.Label(frame, text="Mot de passe").grid(row=1, column=0)
        pw_entry = tk.Entry(frame, show="*")
        pw_entry.grid(row=1, column=1)

        def try_login():
            email = email_entry.get().strip()
            pw = pw_entry.get().strip()
            if email in self.users and self.users[email].check_password(pw):
                self.current_user = self.users[email]
                messagebox.showinfo("Succès", f"Bienvenue {self.current_user.nom} !")
                self.build_main_menu()
            else:
                messagebox.showerror("Erreur", "Identifiants invalides")

        tk.Button(self.root, text="Se connecter", command=try_login).pack(pady=5)
        tk.Button(self.root, text="S'inscrire", command=self.build_register).pack()

    def build_register(self):
        self.clear()
        tk.Label(self.root, text="YuppiQuiz — Inscription", font=("Arial", 18)).pack(pady=10)

        frame = tk.Frame(self.root)
        frame.pack(pady=5)
        tk.Label(frame, text="Nom").grid(row=0, column=0)
        nom_entry = tk.Entry(frame); nom_entry.grid(row=0, column=1)
        tk.Label(frame, text="Email").grid(row=1, column=0)
        email_entry = tk.Entry(frame); email_entry.grid(row=1, column=1)
        tk.Label(frame, text="Mot de passe").grid(row=2, column=0)
        pw_entry = tk.Entry(frame, show="*"); pw_entry.grid(row=2, column=1)

        role_var = tk.StringVar(value="joueur")
        tk.Radiobutton(self.root, text="Joueur", variable=role_var, value="joueur").pack()
        tk.Radiobutton(self.root, text="Créateur", variable=role_var, value="createur").pack()

        def do_register():
            nom = nom_entry.get().strip()
            email = email_entry.get().strip()
            pw = pw_entry.get().strip()
            role = role_var.get()
            if not nom or not email or not pw:
                messagebox.showerror("Erreur", "Remplis tous les champs")
                return
            if email in self.users:
                messagebox.showerror("Erreur", "Email déjà utilisé")
                return
            user = Utilisateur.create(nom=nom, email=email, mot_de_passe=pw, role=role)
            self.users[email] = user
            storage.save_users(self.users)
            messagebox.showinfo("Succès", "Compte créé")
            self.build_login()

        tk.Button(self.root, text="Créer le compte", command=do_register).pack(pady=5)
        tk.Button(self.root, text="Retour", command=self.build_login).pack()

    def build_main_menu(self):
        self.clear()
        tk.Label(self.root, text=f"Bonjour {self.current_user.nom} ({self.current_user.role})", font=("Arial", 16)).pack(pady=10)

        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=5)
        tk.Button(btn_frame, text="Rejoindre un quiz", width=20, command=self.join_quiz).grid(row=0, column=0, padx=5, pady=5)
        tk.Button(btn_frame, text="Voir mes historiques", width=20, command=self.show_history).grid(row=0, column=1, padx=5, pady=5)
        tk.Button(btn_frame, text="Voir classement (par quiz)", width=20, command=self.show_leaderboards).grid(row=1, column=0, padx=5, pady=5)
        if self.current_user.role == "createur":
            tk.Button(btn_frame, text="Créer un quiz", width=20, command=self.create_quiz).grid(row=1, column=1, padx=5, pady=5)
            tk.Button(btn_frame, text="Gérer mes quiz", width=20, command=self.manage_my_quizzes).grid(row=2, column=0, padx=5, pady=5)
        tk.Button(self.root, text="Déconnexion", command=self.logout).pack(pady=10)

    def logout(self):
        self.current_user = None
        self.build_login()

    def create_quiz(self):
        titre = simpledialog.askstring("Création quiz", "Titre du quiz :")
        if not titre:
            return
        # unique pin
        pin = storage.make_unique_pin()
        quiz = Quiz(id=pin, titre=titre, createur_email=self.current_user.email, questions=[], date_creation=time.time())
        # add questions
        while True:
            qtext = simpledialog.askstring("Nouvelle question", "Texte de la question (laisser vide pour finir) :")
            if not qtext:
                break
            reponses = []
            for i in range(4):
                r = simpledialog.askstring("Réponse", f"Option {i+1} :")
                reponses.append(r or "")
            while True:
                try:
                    bonne = simpledialog.askinteger("Bonne réponse", "Indice de la bonne réponse (1-4) :")
                    if bonne and 1 <= bonne <= 4:
                        break
                except:
                    pass
            q = Question(texte=qtext, reponses=reponses, indice_bonne=bonne-1)
            quiz.questions.append(q)
        self.quizzes[quiz.id] = quiz
        storage.save_quizzes(self.quizzes)
        messagebox.showinfo("Quiz créé", f"Quiz '{titre}' créé avec code PIN : {quiz.id}")

    def manage_my_quizzes(self):
        self.clear()
        tk.Label(self.root, text="Mes quiz", font=("Arial", 16)).pack(pady=10)
        frame = tk.Frame(self.root); frame.pack()
        # list creator's quizzes
        my = [q for q in self.quizzes.values() if q.createur_email == self.current_user.email]
        for i, q in enumerate(my):
            txt = f"{q.titre} (PIN {q.id}) - {len(q.questions)} questions"
            label = tk.Label(frame, text=txt)
            label.grid(row=i, column=0, sticky="w", padx=5, pady=2)
            tk.Button(frame, text="Supprimer", command=lambda qq=q: self.delete_quiz(qq)).grid(row=i, column=1)
            tk.Button(frame, text="Modifier", command=lambda qq=q: self.edit_quiz(qq)).grid(row=i, column=2)
        tk.Button(self.root, text="Retour", command=self.build_main_menu).pack(pady=10)

    def edit_quiz(self, quiz):
        # Simple editor: allow adding new question
        qtext = simpledialog.askstring("Ajouter question", "Texte de la question :")
        if not qtext:
            return
        reponses = []
        for i in range(4):
            r = simpledialog.askstring("Réponse", f"Option {i+1} :")
            reponses.append(r or "")
        bonne = simpledialog.askinteger("Bonne réponse", "Indice de la bonne réponse (1-4) :")
        if not (bonne and 1<=bonne<=4):
            messagebox.showerror("Erreur", "Indice invalide")
            return
        q = Question(texte=qtext, reponses=reponses, indice_bonne=bonne-1)
        quiz.questions.append(q)
        self.quizzes[quiz.id] = quiz
        storage.save_quizzes(self.quizzes)
        messagebox.showinfo("OK", "Question ajoutée")


    def delete_quiz(self, quiz):
        if messagebox.askyesno("Confirmer", f"Supprimer le quiz '{quiz.titre}' ?"):
            self.quizzes.pop(quiz.id, None)
            # also remove related scores
            to_delete = [k for k,v in self.scores.items() if v.get("quiz_id")==quiz.id]
            for k in to_delete:
                self.scores.pop(k, None)
            storage.save_quizzes(self.quizzes)
            storage.save_scores(self.scores)
            messagebox.showinfo("OK", "Quiz supprimé")
            self.manage_my_quizzes()

    def join_quiz(self):
        code = simpledialog.askstring("Rejoindre quiz", "Entre le code PIN :")
        if not code:
            return
        if code not in self.quizzes:
            messagebox.showerror("Erreur", "Quiz introuvable")
            return
        quiz = self.quizzes[code]
        # Shuffle questions for randomness without modifying stored order
        questions = quiz.questions.copy()
        random_order = list(range(len(questions)))
        random.shuffle(random_order)

        points = 0
        for idx in random_order:
            q = questions[idx]
            # build display string
            opts = "\n".join([f"{i+1}. {o}" for i,o in enumerate(q.reponses)])
            rep = simpledialog.askinteger("Question", f"{q.texte}\n\n{opts}\n\nIndice de la réponse (1-4) :")
            if rep is None:
                # user cancelled -> stop early
                break
            if rep-1 == q.indice_bonne:
                points += 1
        total = len(questions)
        # save score
        score_id = str(int(time.time()*1000))
        sc = {
            "quiz_id": quiz.id,
            "joueur_email": self.current_user.email,
            "points": points,
            "total": total,
            "date": time.time()
        }
        self.scores[score_id] = sc
        storage.save_scores(self.scores)
        messagebox.showinfo("Résultat", f"Score : {points}/{total}")

    def show_leaderboards(self):
        self.clear()
        tk.Label(self.root, text="Classements par quiz", font=("Arial", 16)).pack(pady=10)
        frame = tk.Frame(self.root); frame.pack(pady=5)
        # for each quiz show top 5
        for i, quiz in enumerate(self.quizzes.values()):
            tk.Label(frame, text=f"{quiz.titre} (PIN {quiz.id})").grid(row=2*i, column=0, sticky="w")
            # compute scores for this quiz
            scores_for = [v for v in self.scores.values() if v.get("quiz_id")==quiz.id]
            scores_for.sort(key=lambda x: (-x["points"], x["date"]))
            text = "\n".join([f"{j+1}. {s['joueur_email']} : {s['points']}/{s['total']}" for j,s in enumerate(scores_for[:5])]) or "Aucun score"
            tk.Label(frame, text=text).grid(row=2*i+1, column=0, sticky="w", padx=10)
        tk.Button(self.root, text="Retour", command=self.build_main_menu).pack(pady=10)

    def show_history(self):
        self.clear()
        tk.Label(self.root, text="Historique des parties", font=("Arial", 16)).pack(pady=10)
        frame = tk.Frame(self.root); frame.pack()
        my_scores = [v for v in self.scores.values() if v.get("joueur_email")==self.current_user.email]
        my_scores.sort(key=lambda x: -x["date"])
        for i, s in enumerate(my_scores):
            quiz = self.quizzes.get(s["quiz_id"])
            titre = quiz.titre if quiz else s["quiz_id"]
            t = time.strftime("%Y-%m-%d %H:%M", time.localtime(s["date"]))
            tk.Label(frame, text=f"{i+1}. {titre} — {s['points']}/{s['total']} — {t}").pack(anchor="w")
        tk.Button(self.root, text="Retour", command=self.build_main_menu).pack(pady=10)

    def clear(self):
        for w in self.root.winfo_children():
            w.destroy()

if __name__ == "__main__":
    storage.ensure_data_dir()
    root = tk.Tk()
    app = YuppiQuizApp(root)
    root.mainloop()
