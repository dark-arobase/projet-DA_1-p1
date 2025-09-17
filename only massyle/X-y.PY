import tkinter as tk
from tkinter import simpledialog, colorchooser
import json
import os

CONFIG_FILE = "button_config.json"

# Charger la configuration depuis un fichier JSON
def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    return {
        "x": 100,
        "y": 100,
        "text": "Mon Bouton",
        "bg": "black",
        "fg": "white",
        "anchor": "center"
    }

# Sauvegarder la configuration dans un fichier JSON
def save_config():
    config = {
        "x": button.winfo_x(),
        "y": button.winfo_y(),
        "text": button["text"],
        "bg": button["bg"],
        "fg": button["fg"],
        "anchor": current_anchor
    }
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=4)
    update_code_label()

# Modifier les propriétés du bouton
def modify_button():
    new_text = simpledialog.askstring("Modifier le texte", "Nouveau texte :", initialvalue=button["text"])
    if new_text:
        button.config(text=new_text)

    new_fg = colorchooser.askcolor(title="Choisir la couleur du texte")[1]
    if new_fg:
        button.config(fg=new_fg)

    new_bg = colorchooser.askcolor(title="Choisir la couleur du fond")[1]
    if new_bg:
        button.config(bg=new_bg)

    save_config()

# Mettre à jour le label qui montre le code .place(...)
def update_code_label():
    x = button.winfo_x()
    y = button.winfo_y()
    code = f'button.place(x={x}, y={y}, anchor="{current_anchor}")'
    label_code.config(text=code)

# Déplacement
def start_drag(event):
    button.startX = event.x
    button.startY = event.y

def on_drag(event):
    dx = event.x - button.startX
    dy = event.y - button.startY
    new_x = button.winfo_x() + dx
    new_y = button.winfo_y() + dy
    button.place(x=new_x, y=new_y, anchor=current_anchor)
    update_code_label()

def on_release(event):
    save_config()

# Fenêtre principale
root = tk.Tk()
root.geometry("700x450")
root.title("Éditeur de bouton Tkinter - Positionnement absolu")

# Charger la configuration
config = load_config()
current_anchor = config.get("anchor", "center")

# Label avec le code .place(...)
label_code = tk.Label(root, text="", font=("Courier", 12), fg="green")
label_code.pack(pady=5)

# Créer le bouton
button = tk.Button(root, text=config["text"], bg=config["bg"], fg=config["fg"], padx=10, pady=5)
button.place(x=config["x"], y=config["y"], anchor=current_anchor)

# Lier les événements
button.bind("<Button-1>", start_drag)
button.bind("<B1-Motion>", on_drag)
button.bind("<ButtonRelease-1>", on_release)

# Bouton de modification
btn_modifier = tk.Button(root, text="Modifier le bouton", command=modify_button)
btn_modifier.pack(pady=10)

# Mettre à jour l’affichage du code place(...)
update_code_label()

root.mainloop()
