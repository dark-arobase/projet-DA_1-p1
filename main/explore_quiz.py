import tkinter as tk

def page_explorer_quiz(root, nom=None, retour=None):
    frame = tk.Frame(root, bg="black")
    label = tk.Label(frame, text="Page Explorer Quiz", font=("Arial", 20), fg="white", bg="black")
    label.pack(pady=20)

    def retour_accueil():
        frame.pack_forget()
        if retour:
            retour.pack(fill="both", expand=True)

    btn_retour = tk.Button(frame, text="Retour", command=retour_accueil)
    btn_retour.pack(pady=10)

    return frame

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Test - Page Explorer Quiz")
    root.geometry("800x600")
    root.configure(bg="black")
    main_frame = page_explorer_quiz(root)
    main_frame.pack(fill="both", expand=True)
    root.mainloop()
