import tkinter as tk
from tkinter import messagebox
import json
import os

def page_modification_quiz(root, nom, retour=None):
    frame = tk.Frame(root, bg="black")
    root.title("Modification de quiz")
    frame.pack(fill="both", expand=True)

    label = tk.Label(frame, text="Page Modification Quiz", font=("Arial", 20), bg="black", fg="white")
    label.pack(pady=20)

    quiz_data = []
    current_quiz = None

    json_path = "main/data/quiz.json"
    if not os.path.exists(json_path):
        tk.Label(frame, text="Fichier quiz.json introuvable", fg="black", bg="white").pack()
        return frame

    with open(json_path, "r", encoding="utf-8") as f:
        quiz_data = json.load(f)

    # Liste de tous les quiz
    listbox = tk.Listbox(frame, width=30, height=10, font=("Arial", 14))
    listbox.pack(pady=10)

    for quiz in quiz_data:
        listbox.insert(tk.END, quiz["titre"])

    # Zone d’édition pour les questions avec scrollbar
    canvas = tk.Canvas(frame, bg="black")
    scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="black")

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    question_widgets = []

    def afficher_quiz(index):
        nonlocal current_quiz
        current_quiz = quiz_data[index]

        # Effacer anciens widgets
        for w in question_widgets:
            w.destroy()
        question_widgets.clear()

        for i, q in enumerate(current_quiz["questions"]):
            q_label = tk.Label(scrollable_frame, text=f"Question {i+1} :", fg="white", bg="black", font=("Arial", 12, "bold"))
            q_label.pack(anchor="w", padx=10, pady=(10, 0))
            question_widgets.append(q_label)

            q_text = tk.Text(scrollable_frame, height=2, width=70)
            q_text.insert("1.0", q["question"])
            q_text.pack(padx=10)
            question_widgets.append(q_text)

            choix_label = tk.Label(scrollable_frame, text="Choix (séparés par ;) :", fg="white", bg="black")
            choix_label.pack(anchor="w", padx=10, pady=(5, 0))
            question_widgets.append(choix_label)

            choix_entry = tk.Entry(scrollable_frame, width=70)
            choix_entry.insert(0, ";".join(q["choix"]))
            choix_entry.pack(padx=10)
            question_widgets.append(choix_entry)

            reponse_label = tk.Label(scrollable_frame, text="Réponse :", fg="white", bg="black")
            reponse_label.pack(anchor="w", padx=10, pady=(5, 0))
            question_widgets.append(reponse_label)

            reponse_entry = tk.Entry(scrollable_frame, width=70)
            reponse_entry.insert(0, q["reponse"])
            reponse_entry.pack(padx=10)
            question_widgets.append(reponse_entry)

            sep = tk.Label(scrollable_frame, text="-" * 70, fg="gray", bg="black")
            sep.pack(pady=5)
            question_widgets.append(sep)

    def sauvegarder():
        if not current_quiz:
            messagebox.showerror("Erreur", "Veuillez sélectionner un quiz d'abord.")
            return

        idx = 0
        for i in range(len(current_quiz["questions"])):
            q_text = question_widgets[idx+1].get("1.0", "end").strip()
            choix_text = question_widgets[idx+3].get().strip()
            reponse_text = question_widgets[idx+5].get().strip()

            current_quiz["questions"][i]["question"] = q_text
            current_quiz["questions"][i]["choix"] = [c.strip() for c in choix_text.split(";") if c.strip()]
            current_quiz["questions"][i]["reponse"] = reponse_text

            idx += 7

        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(quiz_data, f, indent=4, ensure_ascii=False)

        messagebox.showinfo("Succès", "Quiz sauvegardé avec succès !")

    # Frame pour les boutons en bas
    bottom_frame = tk.Frame(frame, bg="black")
    bottom_frame.pack(fill="x", side="bottom", pady=15)

    btn_save = tk.Button(bottom_frame, text="Sauvegarder les modifications",
                         command=sauvegarder, bg="black", fg="white", font=("Arial", 14))
    btn_save.pack(side="left", padx=20)

    def on_select(event):
        selection = event.widget.curselection()
        if selection:
            index = selection[0]
            afficher_quiz(index)

    listbox.bind("<<ListboxSelect>>", on_select)

    def retour_accueil():
        frame.pack_forget()
        if retour:
            retour.pack(fill="both", expand=True)

    btn_retour = tk.Button(bottom_frame, text="Retour", command=retour_accueil,
                           bg="black", fg="white", font=("Arial", 14), width=10)
    btn_retour.pack(side="right", padx=20)

    return frame

# pour tester
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Test - Modification Quiz")
    root.geometry("900x700")
    root.configure(bg="black")
    frame = page_modification_quiz(root, nom="Admin")
    frame.pack(fill="both", expand=True)
    root.mainloop()
