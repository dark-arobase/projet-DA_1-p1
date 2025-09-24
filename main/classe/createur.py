

# Tkinter Frame for quiz creation (to use in your main app)
import tkinter as tk
from tkinter import messagebox
import datetime
import json

class CreerQuizFrame(tk.Frame):
    def __init__(self, parent, retour=None, *args, **kwargs):
        super().__init__(parent, bg="white", *args, **kwargs)
        self.retour = retour

        tk.Label(self, text="Création d'un Quiz", font=("Arial", 18, "bold"), fg="orange", bg="white").pack(pady=10)

        form = tk.Frame(self, bg="white")
        form.pack(pady=10)

        tk.Label(form, text="Titre du Quiz:", bg="white").grid(row=0, column=0, sticky="e")
        self.entry_title = tk.Entry(form)
        self.entry_title.grid(row=0, column=1, pady=5)

        tk.Label(form, text="ID du Quiz:", bg="white").grid(row=1, column=0, sticky="e")
        self.entry_id = tk.Entry(form)
        self.entry_id.grid(row=1, column=1, pady=5)

        tk.Label(form, text="Nombre de questions:", bg="white").grid(row=2, column=0, sticky="e")
        self.entry_nq = tk.Entry(form)
        self.entry_nq.grid(row=2, column=1, pady=5)

        self.questions_frame = tk.Frame(self, bg="white")
        self.questions_frame.pack(pady=10)

        self.add_questions_btn = tk.Button(self, text="Ajouter les questions", command=self.add_questions, bg="blue", fg="white")
        self.add_questions_btn.pack(pady=5)

        self.save_btn = tk.Button(self, text="Enregistrer le quiz", command=self.save_quiz, bg="green", fg="white")
        self.save_btn.pack(pady=10)

        if self.retour:
            tk.Button(self, text="Retour", command=self.retour, bg="gray", fg="white").pack(pady=5)

        self.questions_entries = []

    def add_questions(self):
        for widget in self.questions_frame.winfo_children():
            widget.destroy()
        self.questions_entries.clear()
        try:
            n = int(self.entry_nq.get())
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer un nombre valide de questions.")
            return
        for i in range(n):
            q_label = tk.Label(self.questions_frame, text=f"Question {i+1}:", bg="white")
            q_label.grid(row=i*3, column=0, sticky="w")
            q_entry = tk.Entry(self.questions_frame, width=40)
            q_entry.grid(row=i*3, column=1)
            choix_label = tk.Label(self.questions_frame, text="Choix (séparés par ;):", bg="white")
            choix_label.grid(row=i*3+1, column=0, sticky="w")
            choix_entry = tk.Entry(self.questions_frame, width=40)
            choix_entry.grid(row=i*3+1, column=1)
            rep_label = tk.Label(self.questions_frame, text="Réponse correcte:", bg="white")
            rep_label.grid(row=i*3+2, column=0, sticky="w")
            rep_entry = tk.Entry(self.questions_frame, width=40)
            rep_entry.grid(row=i*3+2, column=1)
            self.questions_entries.append((q_entry, choix_entry, rep_entry))

    def save_quiz(self):
        titre = self.entry_title.get()
        quiz_id = self.entry_id.get()
        date = str(datetime.date.today())
        questions = []
        for q_entry, choix_entry, rep_entry in self.questions_entries:
            question = q_entry.get()
            choix = [c.strip() for c in choix_entry.get().split(';')]
            reponse = rep_entry.get()
            questions.append({
                "question": question,
                "choix": choix,
                "reponse": reponse
            })
        new_quiz = {
            "id": quiz_id,
            "date creation": date,
            "titre": titre,
            "questions": questions
        }
        try:
            with open("quiz.json", 'r', encoding="utf-8") as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []
        data.append(new_quiz)
        with open("quiz.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=3, ensure_ascii=False)
        messagebox.showinfo("Succès", "Quiz enregistré avec succès !")
            