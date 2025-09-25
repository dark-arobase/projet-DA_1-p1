import tkinter as tk
import interface_jeu

def page_explorer_quiz(root, nom=None, retour=None):
    frame = tk.Frame(root, bg="black")
    frame.pack(fill="both", expand=True)
    
    navbar = tk.Frame(frame, bg="black", height=50)
    navbar.pack(fill="x")

    # Espace utilisateur à droite
    user_frame = tk.Frame(navbar, bg="gray")
    user_frame.pack(side="right", padx=10)

    user_label = tk.Label(user_frame, text=f"{nom}, (admin)", fg="white", bg="black")
    user_label.pack(side="left", padx=5)

    # Titre
    label = tk.Label(frame, text="Page Explorer Quiz",
                     font=("Arial", 20, "bold"), fg="white", bg="black")
    label.pack(pady=20)

    # Conteneur central
    center_frame = tk.Frame(frame, bg="black")
    center_frame.pack(expand=True)  # prend tout l'espace restant

    # Gros bouton quiz  ##-----principal probleme rencontrée-----##
    quiz_btn = tk.Button(center_frame,text="Mathematique",font=("Arial", 20, "bold"),
                         bg= "black",fg="white",width=12, height=3,relief="raised", bd=4
                         , command=lambda : changer_page(frame, interface_jeu.page_joueur(root, nom, retour=frame, texte=quiz_btn["text"] )))
    quiz_btn.pack(pady=20)

    # Bouton retour en bas
    def retour_accueil():
        frame.pack_forget()
        if retour:
            retour.pack(fill="both", expand=True)

    btn_retour = tk.Button(frame, text="Retour",
                           command=retour_accueil,
                           font=("Arial", 14, "bold"),
                           bg="red", fg="white", width=10)
    btn_retour.pack(pady=20)

    def changer_page(frame_actuel, frame_suivant):
     frame_actuel.pack_forget()
     frame_suivant.pack(fill="both", expand=True)

    return frame


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Test - Page Explorer Quiz")
    root.geometry("800x600")
    root.configure(bg="black")

    main_frame = page_explorer_quiz(root)
    main_frame.pack(fill="both", expand=True)

    root.mainloop()
