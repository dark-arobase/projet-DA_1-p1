import tkinter as tk

root = None
frame_inscription = None
frame_accueil = None

def set_root(r):
    global root
    root = r

def set_accueil(f_accueil):
    global frame_accueil
    frame_accueil = f_accueil

def creer_inscription():
    global frame_inscription
    frame_inscription = tk.Frame(root, bg="white")

    label = tk.Label(frame_inscription, text="PAGE INSCRIPTION", font=("Arial", 24, "bold"), bg="white")
    label.pack(pady=40)

    label1 = tk.Label(frame_inscription, text="Test inscription", bg="white")
    label1.pack(pady=5)

    commentaire = tk.Entry(frame_inscription)
    commentaire.pack(pady=20)

    btn_envoyer = tk.Button(frame_inscription, text="Inscription", bg="black", fg="white", font=("Arial", 10, "bold"))
    btn_envoyer.pack(pady=10)

    btn_retour = tk.Button(frame_inscription, text="Retour à l'accueil", bg="black", fg="white", font=("Arial", 10, "bold"), command=montrer_accueil)
    btn_retour.pack(pady=20)

    return frame_inscription

def montrer_inscription():
    frame_accueil.pack_forget()
    if frame_inscription:
        frame_inscription.pack(fill="both", expand=True)

def montrer_accueil():
    if frame_inscription:
        frame_inscription.pack_forget()
    frame_accueil.pack(fill="both", expand=True)
