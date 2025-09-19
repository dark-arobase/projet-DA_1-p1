import tkinter as tk
from PIL import Image, ImageTk #pip install pillow

# Créer la fenêtre principale
root = tk.Tk()
root.title("Yuppiquiz")
root.geometry("600x600")
root.configure(bg="black")

# Charger et afficher une image
img = Image.open("main/img/pattern.png")
photo = ImageTk.PhotoImage(img)
img_label = tk.Label(root, image=photo, bg="black")
img_label.image = photo  # Nécessaire pour empêcher le garbage collection
img_label.pack()

# Créer un rectangle (frame) centré
frame = tk.Frame(root, width=320, height=360, bg="black", highlightthickness=2, highlightbackground="white")
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
# Ajouter une phrase dans le rectangle
label_title = tk.Label(frame, text="Bienvenue sur Yuppiquiz !", bg="black", fg="white", font=("Arial", 14, "bold"))
label_title.pack(pady=(30, 10))

label_desc = tk.Label(frame, text="Testez vos connaissances et amusez-vous.", bg="black", fg="white", font=("Arial", 11))
label_desc.pack(pady=(0, 30))

# Ajouter des boutons dans le rectangle
btn_inscription = tk.Button(frame, text="INSCRIPTION", bg="white", fg="black", font=("Arial", 12, "bold"))
btn_inscription.pack(pady=10)

btn_connexion = tk.Button(frame, text="SE CONNECTER", bg="white", fg="black", font=("Arial", 12, "bold"))
btn_connexion.pack(pady=10)

# Exemple de bouton à l'extérieur du rectangle (frame)
btn_exterieur = tk.Button(root, text="Bouton extérieur", bg="white", fg="black", font=("Arial", 12, "bold"))
btn_exterieur.place(x=0, y=0)  # Position absolue (x, y) dans la fenêtre principale
    

# Boucle principale
root.mainloop()
