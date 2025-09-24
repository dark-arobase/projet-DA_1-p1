import tkinter as tk

def page_cree_quiz(root, nom, retour=None):
    frame = tk.Frame(root, bg="white")
    label = tk.Label(frame, text="Page Créer Quiz", font=("Arial", 20), bg="white", fg="black")
    label.pack(pady=20)

    def retour_accueil():
        frame.pack_forget()
        if retour:
            retour.pack(fill="both", expand=True)

    btn_retour = tk.Button(frame, text="Retour", command=retour_accueil, bg="black", fg="white")
    btn_retour.pack(pady=10)

    # Ici tu peux rajouter ton formulaire ou contenu pour créer un quiz

    return frame

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Test - Créer Quiz")
    root.geometry("800x600")
    root.configure(bg="white")
    frame = page_cree_quiz(root, nom="TOTO")
    frame.pack(fill="both", expand=True)
    root.mainloop()
