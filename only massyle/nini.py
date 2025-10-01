import tkinter as tk
import re

root = tk.Tk()
root.title("Menu principal")
root.geometry("400x400")
#root.attributes('-fullscreen', True)
#root.configure(bg="#a2d5f2")

titre=tk.Label(root, text="liste inscription", font=("Arial", 24, "bold"))
titre.grid(row=0, column=0, columnspan=2, pady=10)


name_label=tk.Label(root, text="nom : ")
name_label.grid(row=1, column=0)

name_entry=tk.Entry(root)
name_entry.grid(row=1, column=1)

name_message=tk.Label(root, text="", fg="red")
name_message.grid(row=1, column=2)

prenom_label=tk.Label(root, text="prenom : ")
prenom_label.grid(row=2, column=0)

prenom_entry=tk.Entry(root)
prenom_entry.grid(row=2, column=1)

prenom_message=tk.Label(root, text="", fg="red")
prenom_message.grid(row=2, column=2)

email_label=tk.Label(root, text="email : ")
email_label.grid(row=3, column=0)

email_entry=tk.Entry(root)
email_entry.grid(row=3, column=1)

email_message=tk.Label(root, text="", fg="red")
email_message.grid(row=3, column=2)

mdp_label=tk.Label(root, text="mot de passe : ")
mdp_label.grid(row=4, column=0)

mdp_entry=tk.Entry(root, show="*")
mdp_entry.grid(row=4, column=1)

mdp_message=tk.Label(root, text="", fg="red")
mdp_message.grid(row=4, column=2)

mdp2_label=tk.Label(root, text="confirmer mot de passe : ")
mdp2_label.grid(row=5, column=0)

mdp2_entry=tk.Entry(root, show="*")
mdp2_entry.grid(row=5, column=1)

mdp2_message=tk.Label(root, text="", fg="red")
mdp2_message.grid(row=5, column=2)


def valider():
    nom = name_entry.get()
    prenom = prenom_entry.get()
    email = email_entry.get()
    mdp = mdp_entry.get()
    mdp2 = mdp2_entry.get()

    if nom is not None and re.match(r"^[a-zA-Z]{3,}$", nom):
        name_message.config(text="Nom valide",fg="green")
    else:
        name_message.config(text="Nom invalide",fg="red")

    if prenom is not None and re.match(r"^[a-zA-Z]{3,}$", prenom):
        prenom_message.config(text="Prenom valide",fg="green")
    else:
        prenom_message.config(text="Prenom invalide",fg="red")

    if email is not None and re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
        email_message.config(text="Email valide",fg="green")
    else:
        email_message.config(text="Email invalide",fg="red")
    
    if mdp is not None and re.match(r"^[a-zA-Z0-9]{6,}$", mdp):
        mdp_message.config(text="Mot de passe valide",fg="green")
    else:
        mdp_message.config(text="Mot de passe invalide",fg="red")
    
    if mdp2 is not None and re.match(r"^[a-zA-Z0-9]{6,}$", mdp2):
        mdp2_message.config(text="Mot de passe valide",fg="green")
    else:
        mdp2_message.config(text="Mot de passe invalide",fg="red")
    if mdp == mdp2:
        mdp2_message.config(text="Mot de passe identique",fg="green")
    else:
        mdp2_message.config(text="Mot de passe différent",fg="red")


ins=tk.Button(root, text="S'inscrire",command=valider).grid(row=6, column=0)
annuler=tk.Button(root, text="annuler",command=root.quit).grid(row=6, column=1)


root.mainloop()