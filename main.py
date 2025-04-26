import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import torch
import os
import glob

# Charger YOLOv5
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True, trust_repo=True)

# Créer la fenêtre
root = tk.Tk()
root.title("YOLOv5 Object Detection 🚀")
root.geometry("1200x800")
root.config(bg="#1e1e2f")  # Fond moderne foncé

# Style global
font_title = ("Poppins", 26, "bold")
font_button = ("Poppins", 14, "bold")
font_normal = ("Poppins", 12)

# Header
header = tk.Frame(root, bg="#28293e", height=80)
header.pack(fill="x")

title = tk.Label(header, text="🛰️ Détection d'Objets avec YOLOv5", bg="#28293e", fg="white", font=font_title)
title.pack(pady=20)

# Contenu principal
main_frame = tk.Frame(root, bg="#1e1e2f")
main_frame.pack(fill="both", expand=True, padx=20, pady=20)

# Zone pour l'image détectée
img_card = tk.Frame(main_frame, bg="#28293e", bd=2, relief="ridge")
img_card.pack(pady=20)

img_label = tk.Label(img_card, bg="#28293e")
img_label.pack(padx=20, pady=20)

# Bouton stylé
def on_enter(e):
    detect_button['background'] = '#5dade2'
def on_leave(e):
    detect_button['background'] = '#3498db'

def charger_et_detecter():
    file_path = filedialog.askopenfilename(
        title="Choisir une image",
        filetypes=[("Fichiers image", "*.jpg *.jpeg *.png *.bmp")]
    )
    if file_path:
        results = model(file_path)
        results.save()

        detect_path = os.path.join('runs', 'detect')
        latest_exp = max(glob.glob(os.path.join(detect_path, 'exp*')), key=os.path.getmtime)

        detected_images = glob.glob(os.path.join(latest_exp, '*.jpg'))
        if detected_images:
            detected_img_path = detected_images[0]
            img = Image.open(detected_img_path)
            img.thumbnail((1000, 600))
            img_tk = ImageTk.PhotoImage(img)
            img_label.configure(image=img_tk)
            img_label.image = img_tk

detect_button = tk.Button(root, text="📸 Charger une Image", font=font_button, bg="#3498db", fg="white",
                          activebackground="#5dade2", activeforeground="white",
                          padx=20, pady=10, bd=0, command=charger_et_detecter, cursor="hand2")

detect_button.pack(pady=10)
detect_button.bind("<Enter>", on_enter)
detect_button.bind("<Leave>", on_leave)

root.mainloop()
