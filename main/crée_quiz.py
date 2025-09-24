import tkinter as tk
from tkinter import messagebox
import datetime
import json

def page_cree_quiz(root, nom, retour=None):
    frame = tk.Frame(root, bg="black")
    label = tk.Label(frame, text="Page Créer Quiz", font=("Arial", 20), bg="white", fg="black")
    label.pack(pady=20)

    def retour_accueil():
        frame.pack_forget()
        if retour:
            retour.pack(fill="both", expand=True)

    btn_retour = tk.Button(frame, text="Retour", command=retour_accueil, bg="black", fg="white")
    btn_retour.pack(pady=10)

    # Ici tu peux rajouter ton formulaire ou contenu pour créer un qui

    tk.Label(frame, text="Création d'un Quiz", font=("Arial", 18, "bold"), fg="Black", bg="white").pack(pady=10)

    form = tk.Frame(frame, bg="black")
    form.pack(pady=10)

    tk.Label(form, text="Titre du Quiz:",bg="black", fg="white").grid(row=0, column=0, sticky="e")
    entry_title = tk.Entry(form)
    entry_title.grid(row=0, column=1, pady=5)

    tk.Label(form, text="ID du Quiz:", bg="black", fg="white").grid(row=1, column=0, sticky="e")
    entry_id = tk.Entry(form)
    entry_id.grid(row=1, column=1, pady=5)

    tk.Label(form, text="Nombre de questions:", bg="black", fg="white").grid(row=2, column=0, sticky="e")
    entry_nq = tk.Entry(form)
    entry_nq.grid(row=2, column=1, pady=5)

    questions_frame = tk.Frame(frame, bg="black")
    questions_frame.pack(pady=10)

    questions_entries = []  # Liste pour stocker les entrées de questions

    def add_questions():
        for widget in questions_frame.winfo_children():
            widget.destroy()
        questions_entries.clear()
        try:
            n = int(entry_nq.get())
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer un nombre valide de questions.")
            return
        for i in range(n):
            q_label = tk.Label(questions_frame, text=f"Question {i+1}:", bg="black", fg="white")
            q_label.grid(row=i*3, column=0, sticky="w")
            q_entry = tk.Entry(questions_frame, width=40)
            q_entry.grid(row=i*3, column=1)
            choix_label = tk.Label(questions_frame, text="Choix (séparés par ;):", bg="black", fg="white")
            choix_label.grid(row=i*3+1, column=0, sticky="w")
            choix_entry = tk.Entry(questions_frame, width=40)
            choix_entry.grid(row=i*3+1, column=1)
            rep_label = tk.Label(questions_frame, text="Réponse correcte:", bg="black", fg="white")
            rep_label.grid(row=i*3+2, column=0, sticky="w")
            rep_entry = tk.Entry(questions_frame, width=40)
            rep_entry.grid(row=i*3+2, column=1)
            questions_entries.append((q_entry, choix_entry, rep_entry))

    def save_quiz():
        titre = entry_title.get()
        quiz_id = entry_id.get()
        date = str(datetime.date.today())
        questions = []

        if not titre or not quiz_id or not questions_entries:
            messagebox.showerror("Erreur", "Tous les champs doivent être remplis et les questions ajoutées.")
            return

        for q_entry, choix_entry, rep_entry in questions_entries:
            question = q_entry.get()
            choix = [c.strip() for c in choix_entry.get().split(';')]
            reponse = rep_entry.get()

            if not question or not choix or not reponse:
                messagebox.showerror("Erreur", "Veuillez remplir toutes les questions correctement.")
                return

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
            with open("main/data/quiz.json", 'r', encoding="utf-8") as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []

        data.append(new_quiz)
        with open("main/data/quiz.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=3, ensure_ascii=False)

        messagebox.showinfo("Succès", "Quiz enregistré avec succès !")

    add_questions_btn = tk.Button(frame, text="Ajouter les questions", command=add_questions, bg="blue", fg="white")
    add_questions_btn.pack(pady=5)

    save_btn = tk.Button(frame, text="Enregistrer le quiz", command=save_quiz, bg="green", fg="white")
    save_btn.pack(pady=10)

    if retour:
        # Bouton retour vers la page précédente si elle existe
        tk.Button(frame, text="Retour", command=retour_accueil, bg="gray", fg="white").pack(pady=5)

    # fin de la modification

    return frame

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Test - Créer Quiz")
    root.geometry("800x600")
    root.configure(bg="white")
    frame = page_cree_quiz(root, nom="TOTO")
    frame.pack(fill="both", expand=True)
    root.mainloop()

