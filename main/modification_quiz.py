import tkinter as tk

def page_modification_quiz(root, nom, retour=None):
    frame = tk.Frame(root, bg="black")
    label = tk.Label(frame, text="Page Modification Quiz", font=("Arial", 20), bg="black", fg="white")
    label.pack(pady=20)

    def retour_accueil():
        frame.pack_forget()
        if retour:
            retour.pack(fill="both", expand=True)

    btn_retour = tk.Button(frame, text="Retour", command=retour_accueil, bg="black", fg="white")
    btn_retour.pack(pady=10)

    # Ici tu peux mettre les contrôles pour modifier un quiz existant

    return frame

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Test - Modification Quiz")
    root.geometry("800x600")
    root.configure(bg="white")
    frame = page_modification_quiz(root, nom="TOTO")
    frame.pack(fill="both", expand=True)
    root.mainloop()
