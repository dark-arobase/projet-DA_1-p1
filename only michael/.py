import tkinter as tk


root = tk.Tk()
root.title("Quiz Mathématique")
root.geometry("500x500")
root.configure(bg="black")

label = tk.Label(root, text="Quiz Mathématique!", font=("Arial", 24, "bold"), bg="black", fg="white")
label.pack(pady=20)

question_label = tk.Label(root, text="Que font 5x5?", font=("Arial", 18), bg="black", fg="white")
question_label.pack(pady=20)
button_frame = tk.Frame(root, bg="black")
button_frame.pack(pady=20)

button1 = tk.Button(button_frame, text="25", font=("Arial", 16), bg="black", fg="white")
button1.pack(side="left", padx=10)
button2 = tk.Button(button_frame, text="20", font=("Arial", 16), bg="black", fg="white")
button2.pack(side="left", padx=10)  
button3 = tk.Button(button_frame, text="15", font=("Arial", 16), bg="black", fg="white")
button3.pack(side="left", padx=10)
button4 = tk.Button(button_frame, text="10", font=("Arial", 16), bg="black", fg="white")
button4.pack(side="left", padx=10)


















root.mainloop()