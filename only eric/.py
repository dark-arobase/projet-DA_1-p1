import tkinter as tk
import sys

class RedirectStdout:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, message):
        self.text_widget.insert(tk.END, message)
        self.text_widget.see(tk.END)  # Scroll automatique

    def flush(self):
        pass  # Nécessaire pour compatibilité avec certains flux

def exemple_de_fonction():
    for i in range(5):
        print(f"Ligne {i + 1} exécutée")

# Interface Tkinter
fenetre = tk.Tk()
fenetre.title("Affichage du script")

zone_texte = tk.Text(fenetre, height=15, width=60)
zone_texte.pack(padx=10, pady=10)

# Redirection de stdout vers la zone de texte
sys.stdout = RedirectStdout(zone_texte)

# Bouton pour lancer la fonction
bouton = tk.Button(fenetre, text="Exécuter le script", command=exemple_de_fonction)
bouton.pack(pady=5)

fenetre.mainloop()
