import tkinter as tk
from tkinter import messagebox
import random

# Liste de questions mathématiques (question, choix, réponse correcte)
questions = [
    ("Combien fait 5 + 3 ?", ["6", "7", "8", "9"], "8"),
    ("Combien fait 12 - 4 ?", ["6", "7", "8", "9"], "8"),
    ("Quel est le résultat de 6 * 7 ?", ["42", "35", "49", "54"], "42"),
    ("Combien fait 81 ÷ 9 ?", ["7", "8", "9", "10"], "9"),
    ("Quel est le carré de 9 ?", ["81", "72", "90", "100"], "81"),
    ("Combien fait 15 + 6 ?", ["20", "21", "22", "23"], "21"),
    ("Quel est le résultat de 16 ÷ 4 ?", ["3", "4", "5", "6"], "4"),
    ("Combien fait 25 - 10 ?", ["12", "13", "15", "14"], "15"),
    ("Quel est le cube de 3 ?", ["27", "28", "25", "30"], "27"),
    ("Combien fait 9 + 9 ?", ["16", "17", "18", "19"], "18"),
    ("Combien fait 18 ÷ 3 ?", ["5", "6", "7", "8"], "6"),
    ("Quel est le résultat de 5 * 5 ?", ["20", "25", "30", "35"], "25"),
    ("Combien fait 14 + 7 ?", ["19", "20", "21", "22"], "21"),
    ("Quel est le double de 22 ?", ["42", "44", "48", "50"], "44"),
    ("Quel est le résultat de 36 ÷ 6 ?", ["4", "5", "6", "7"], "6"),
    ("Combien fait 7 * 9 ?", ["63", "64", "62", "60"], "63"),
    ("Combien fait 50 ÷ 5 ?", ["8", "9", "10", "11"], "10"),
    ("Quel est le résultat de 11 * 11 ?", ["121", "122", "123", "124"], "121"),
    ("Combien fait 17 + 8 ?", ["24", "25", "26", "27"], "25"),
    ("Quel est le résultat de 100 ÷ 10 ?", ["9", "10", "11", "12"], "10")
]

# Mélanger les questions pour qu'elles apparaissent dans un ordre aléatoire
random.shuffle(questions)

# Variables globales
score = 0
current_question = 0

# Fonction pour vérifier la réponse et passer à la question suivante
def check_answer(selected_answer):
    global current_question, score
    if selected_answer == questions[current_question][2]:
        score += 1
    current_question += 1
    
    if current_question < len(questions):
        show_question()
    else:
        messagebox.showinfo("Quiz terminé", f"Votre score est : {score}/20")
        score = 0
        current_question = 0
        show_home()

# Fonction pour afficher la question et les choix
def show_question():
    global current_question
    question, choices, _ = questions[current_question]
    
    question_label.config(text=question)
    
    # Créer des boutons pour les choix de réponse
    for i in range(4):
        answer_buttons[i].config(text=choices[i], command=lambda ans=choices[i]: check_answer(ans))

# Fonction pour revenir à la page d'accueil après le quiz
def show_home():
    # Cacher la fenêtre du quiz
    question_label.pack_forget()
    for button in answer_buttons:
        button.pack_forget()

    # Afficher l'écran d'accueil
    home_label.pack(pady=20)
    quiz_button_1.pack(pady=10)
    quiz_button_2.pack(pady=10)

# Fonction pour démarrer le quiz
def start_quiz():
    # Cacher l'écran d'accueil
    home_label.pack_forget()
    quiz_button_1.pack_forget()
    quiz_button_2.pack_forget()

    # Afficher la première question du quiz
    question_label.pack(pady=20)
    for button in answer_buttons:
        button.pack(pady=5)
    
    show_question()

# Initialisation de la fenêtre Tkinter
window = tk.Tk()
window.title("Youpy Quiz")

# Passer la fenêtre en mode plein écran
window.attributes("-fullscreen", True)

# Label pour l'écran d'accueil
home_label = tk.Label(window, text="Bienvenue sur Youpy Quiz!\nVeuillez choisir un quiz.", font=("Arial", 24))
home_label.pack(pady=20)

# Boutons pour sélectionner le quiz
quiz_button_1 = tk.Button(window, text="Quiz Mathématique", font=("Arial", 18), width=20, command=start_quiz)
quiz_button_2 = tk.Button(window, text="Autre Quiz", font=("Arial", 18), width=20)

# Label pour afficher la question
question_label = tk.Label(window, text="", font=("Arial", 16))

# Boutons pour les choix de réponse
answer_buttons = [tk.Button(window, text="", font=("Arial", 14), width=20) for _ in range(4)]

# Lancer l'écran d'accueil
show_home()

# Lancer l'application Tkinter
window.mainloop()