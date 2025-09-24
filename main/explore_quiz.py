import tkinter as tk

def page_explorer_quiz(root, nom=None, retour=None):
    frame = tk.Frame(root, bg="black")

    # Titre
    label = tk.Label(frame, text="Page Explorer Quiz",
                     font=("Arial", 20, "bold"), fg="white", bg="black")
    label.pack(pady=20)

    # Conteneur central
    center_frame = tk.Frame(frame, bg="black")
    center_frame.pack(expand=True)  # prend tout l'espace restant

    # Gros bouton quiz
    quiz_btn = tk.Button(center_frame,text="Mathématique",font=("Arial", 20, "bold"),bg= "black",fg="white",width=12, height=3,relief="raised", bd=4)
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

    return frame


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Test - Page Explorer Quiz")
    root.geometry("800x600")
    root.configure(bg="black")

    main_frame = page_explorer_quiz(root)
    main_frame.pack(fill="both", expand=True)

    root.mainloop()
