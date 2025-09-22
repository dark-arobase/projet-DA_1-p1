import tkinter as tk

def creer_inscription(root, retour=None):
    """Crée la frame inscription."""
    frame = tk.Frame(root, bg="black")

    tk.Label(frame, text="PAGE INSCRIPTION", font=("Arial", 24, "bold"), bg="black", fg="white").pack(pady=40)

    tk.Label(frame, text="Nom :", bg="black", font=("Arial", 12), fg="white").pack(pady=5)
    entry_nom = tk.Entry(frame, font=("Arial", 12))
    entry_nom.pack(pady=5)

    tk.Label(frame, text="Email :", bg="black", font=("Arial", 12), fg="white").pack(pady=5)
    entry_email = tk.Entry(frame, font=("Arial", 12))
    entry_email.pack(pady=5)

    def valider_inscription():
        print("Nom :", entry_nom.get())
        print("Email :", entry_email.get())
        with open("main/data/BasedeDonnee.csv", "a", encoding="utf-8") as f:
            f.write(f"{entry_nom.get()},{entry_email.get()}\n")

    tk.Button(frame, text="Inscription", command=valider_inscription,
              bg="black", fg="white", font=("Arial", 12, "bold")).pack(pady=20)

    if retour:
        tk.Button(frame, text="Retour",
                  command=lambda: changer_page(frame, retour),
                  bg="black", fg="white", font=("Arial", 12, "bold")).pack(pady=10)

    return frame

def changer_page(frame_actuel, frame_suivant):
    frame_actuel.pack_forget()
    frame_suivant.pack(fill="both", expand=True)

# Mode test autonome
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")
    frame = creer_inscription(root)
    frame.pack(fill="both", expand=True)
    root.mainloop()
