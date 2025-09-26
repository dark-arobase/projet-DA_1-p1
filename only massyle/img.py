import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os
import threading
import connection
import inscription

class YuppiquizApp:
    def __init__(self, root):
        self.root = root
        root.title("Yuppiquiz")
        root.geometry("900x650")
        root.minsize(700, 500)

        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.bg_image_path = os.path.join(base_dir, "img", "pattern.png")

        self.bg_image_raw = None
        self.bg_img = None

        # Canvas en arrière-plan (rempli toute la fenêtre)
        self.canvas = tk.Canvas(root, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        # Frames (créées dans root pour être au-dessus du Canvas)
        self.frame_accueil = tk.Frame(root, bg="black", bd=2, highlightbackground="white", highlightthickness=2)
        self.frame_inscription = inscription.creer_inscription(root, retour=self.show_accueil)
        self.frame_connexion = connection.connexion_utilisateur(root, retour=self.show_accueil)

        # Contenu frame accueil
        lbl_title = tk.Label(self.frame_accueil, text="Bienvenue sur Yuppiquiz !", bg="black", fg="white",
                             font=("Segoe UI", 22, "bold"))
        lbl_title.pack(pady=(30, 10))

        lbl_subtitle = tk.Label(self.frame_accueil, text="Testez vos connaissances et amusez-vous.", bg="black", fg="white",
                                font=("Segoe UI", 14))
        lbl_subtitle.pack(pady=(0, 20))

        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TButton",
                        background="black",
                        foreground="white",
                        font=("Segoe UI", 12, "bold"),
                        padding=10)
        style.map("TButton",
                  background=[('active', '#444')],
                  foreground=[('active', 'white')])

        btn_inscription = ttk.Button(self.frame_accueil, text="INSCRIPTION", command=self.show_inscription)
        btn_inscription.pack(pady=10, ipadx=20, ipady=8)

        btn_connexion = ttk.Button(self.frame_accueil, text="SE CONNECTER", command=self.show_connexion)
        btn_connexion.pack(pady=10, ipadx=20, ipady=8)

        self.current_frame = None
        self.resize_after_id = None
        root.bind("<Configure>", self.on_resize)

        self.show_accueil()

        threading.Thread(target=self.load_image, daemon=True).start()

    def load_image(self):
        try:
            self.bg_image_raw = Image.open(self.bg_image_path)
        except Exception as e:
            self.bg_image_raw = None
            self.root.after(0, lambda: messagebox.showerror("Erreur", f"Image de fond non trouvée : {self.bg_image_path}\n{e}"))
            return
        self.root.after(0, self.resize_elements)

    def on_resize(self, event):
        if self.resize_after_id:
            self.root.after_cancel(self.resize_after_id)
        self.resize_after_id = self.root.after(200, self.resize_elements)

    def resize_elements(self, event=None):
        w = self.root.winfo_width()
        h = self.root.winfo_height()
        self.canvas.config(width=w, height=h)

        if self.bg_image_raw:
            resized = self.bg_image_raw.resize((w, h), Image.Resampling.LANCZOS)
            self.bg_img = ImageTk.PhotoImage(resized)
            self.canvas.delete("bg")
            self.canvas.create_image(0, 0, image=self.bg_img, anchor="nw", tags="bg")

        if self.current_frame:
            fw, fh = int(w * 0.52), int(h * 0.48)
            self.current_frame.place(relx=0.5, rely=0.5, anchor="center", width=fw, height=fh)

    def show_frame(self, frame):
        if self.current_frame:
            self.current_frame.place_forget()
        self.current_frame = frame
        self.resize_elements()

    def show_accueil(self):
        self.show_frame(self.frame_accueil)

    def show_inscription(self):
        self.show_frame(self.frame_inscription)

    def show_connexion(self):
        self.show_frame(self.frame_connexion)


if __name__ == "__main__":
    root = tk.Tk()
    app = YuppiquizApp(root)
    root.mainloop()
