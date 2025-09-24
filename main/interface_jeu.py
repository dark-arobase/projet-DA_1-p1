import tkinter as tk
import explore_quiz
import crée_quiz 
import modification_quiz
import createur

def page_joueur():
#Fenetre principal root
    frame = tk.Frame(root, bg="white")

    # ------------------------------
    # BARRE DE NAVIGATION EN HAUT
    # ------------------------------
    navbar = tk.Frame(frame, bg="black", height=50)
    navbar.pack(fill="x")

    # Boutons de navigation
    nav_buttons = [("Accueil", lambda: changer_page(frame, createur.creer_accueil_utilisateur(root, nom, retour=frame)))
                   ,("Explorer",lambda: changer_page(frame, explore_quiz.page_explorer_quiz(root, nom, retour=frame))), 
                   ("Mode utilisateur",lambda: changer_page(frame, createur.creer_accueil_utilisateur(root, nom, retour=frame)))]
    for text, cmd in nav_buttons:
        btn = tk.Button(navbar, text=text, command=cmd,
                        bg="black", fg="white", relief="flat", padx=20, pady=10)
        btn.pack(side="left", padx=5, pady=5)


    # (Optionnel) Ajout d'un avatar (image) : ici, juste un rond gris simulé

    Label = tk.Label(root, text="Zone de Quiz", font=("Arial", 24, "bold"), fg="Orange", bg="aqua")
    Label.pack(pady=20)

    def changer_page(frame_actuel, frame_suivant):
      frame_actuel.pack_forget()
      frame_suivant.pack(fill="both", expand=True)

    main_frame=tk.Frame(root, bg="white")
    main_frame.pack(expand=True)



    root.mainloop()

# Mode test autonome
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Test - Zone de jeu")
    root.geometry("800x600")
    root.configure(bg="black")

    frame_test = page_joueur()
    frame_test.pack(fill="both", expand=True)

    root.mainloop()