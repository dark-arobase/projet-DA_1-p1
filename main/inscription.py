import tkinter as tk

def creer_inscription(root, retour=None):
    """Crée la frame inscription."""
    frame = tk.Frame(root, bg="black")
    root.title("Inscription")

    box_text_font = ("Arial", 12)

    '''# Frame centrale avec rectangle blanc
    frame_centre = tk.Frame(frame, bg="black", width=350, height=430, highlightbackground="white",
                        highlightthickness=2)
    frame_centre.place(relx=0.5, rely=0.5, anchor="center")'''

    tk.Label(frame, text="PAGE INSCRIPTION", font=("Arial", 24, "bold"), bg="black", fg="white").pack(pady=40)

    tk.Label(frame, text="Nom d'utilisateur :", bg="black", font=box_text_font, fg="white").pack(pady=5)
    entry_nom = tk.Entry(frame, font=box_text_font)
    entry_nom.pack(pady=5)

    tk.Label(frame, text="Email :", bg="black", font=box_text_font, fg="white").pack(pady=5)
    entry_email = tk.Entry(frame, font=box_text_font)
    entry_email.pack(pady=5)

    # Champ Nouveau mot de passe
    tk.Label(frame, text="Nouveau mot de passe :", bg="black", font=box_text_font, fg="white").pack(pady=5)
    entry_mdp = tk.Entry(frame, font=box_text_font, show="*")
    entry_mdp.pack(pady=5)

    # Champ Confirmation mot de passe
    tk.Label(frame, text="Retaper le mot de passe :", bg="black", font=box_text_font, fg="white").pack(pady=5)
    entry_confirm_mdp = tk.Entry(frame, font=box_text_font, show="*")
    entry_confirm_mdp.pack(pady=5)

    # Label pour message d'erreur ou succès
    label_message = tk.Label(frame, text="", font=box_text_font, fg="red", bg="black")
    label_message.pack(pady=10)

    def valider_inscription():
        nom = entry_nom.get()
        email = entry_email.get()
        mdp = entry_mdp.get()
        confirm_mdp = entry_confirm_mdp.get()

        if not nom or not email or not mdp or not confirm_mdp:
            label_message.config(text="Veuillez remplir tous les champs.", fg="red")
            return
        if mdp != confirm_mdp:
            label_message.config(text="Les mots de passe ne correspondent pas.", fg="red")
            return

        # Enregistrement dans un fichier CSV
        with open("main/data/BasedeDonnee.csv", "a", encoding="utf-8") as f:
            f.write(f"{nom},{email},{mdp}\n")

        label_message.config(text="Inscription réussie !", fg="green")

    tk.Button(frame, text="Inscription", command=valider_inscription,
              bg="white", fg="black", font=("Arial", 12, "bold")).pack(pady=20)
    if retour:
        tk.Button(frame, text="Retour",
                  command=lambda: changer_page(frame, retour),
                  bg="white", fg="black", font=("Arial", 12, "bold")).pack(pady=10)
    return frame

def changer_page(frame_actuel, frame_suivant):
    frame_actuel.pack_forget()
    frame_suivant.pack(fill="both", expand=True)

# Mode test autonome
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")
    root.configure(bg="black")
    frame = creer_inscription(root)
    frame.pack(fill="both", expand=True)
    root.mainloop()
