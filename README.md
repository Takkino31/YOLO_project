Voici un **README.md complet et bien structuré** pour ton projet de détection d’objets avec YOLOv5 et interface Tkinter. Il couvre l’installation, l’activation de l’environnement virtuel selon le système (Windows, macOS, Linux), les dépendances, et le lancement de l’application :

---

```markdown
# YOLOv5 Object Detection with Tkinter GUI

Projet de détection d'objets basé sur l'architecture YOLOv5, avec une interface graphique conviviale développée en Python avec Tkinter.

## 🧠 Objectif

Permettre à l'utilisateur de sélectionner une image depuis son système, d'effectuer une détection d'objets avec YOLOv5, puis d'afficher le résultat dans une fenêtre graphique simple et élégante.

---

## 🔧 Prérequis

- Python 3.8+ recommandé
- Git
- pip
- Accès à internet (pour le téléchargement initial de YOLOv5 depuis le hub PyTorch)

---

## 🚀 Installation du projet

### 1. Cloner le projet

```bash
git clone https://github.com/Takkino31/YOLO_project.git
cd YOLO_project
```

### 2. Créer un environnement virtuel

#### ✅ Sous Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

#### ✅ Sous Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

Le fichier `requirements.txt` contient notamment :

```text
torch>=1.7
torchvision
Pillow
tk
```

> 💡 YOLOv5 est automatiquement chargé via `torch.hub.load`, donc pas besoin de l’installer manuellement.

---

## 🎯 Lancer l'application

Assurez-vous que l’environnement virtuel est activé, puis exécutez :

```bash
python main.py
```

Une fenêtre graphique s’ouvre. Cliquez sur "Charger une image", sélectionnez une image, et YOLOv5 se chargera de la détection. L’image annotée sera affichée dans l’interface.

---

# 🎯 YOLOv5 Object Detection avec Interface Graphique 

Ce projet est une application permettant de détecter des objets sur des images en utilisant **YOLOv5** avec une interface graphique 

---

## 📁 Arborescence du projet

```text
.
├── datasets/              # Contient vos images et étiquettes pour l'entraînement ou tests
│   ├── images/
│   └── labels/
├── models/                 # Modèles personnalisés ou sauvegardés
├── runs/                   # Résultats des détections (généré automatiquement)
├── venv/                   # Environnement virtuel (facultatif)
├── yolo_env/               # Environnement virtuel alternatif
├── yolov5/                 # Dossier cloné de YOLOv5 officiel
├── main.py                 # Script principal pour l'interface
├── README.md               # Ce fichier
├── requirements.txt        # Liste des dépendances
├── .gitignore              # Fichiers à ignorer par Git
└── yolov5s.pt              # Modèle YOLOv5 préentraîné

```text
.
├── main.py                # Interface graphique + détection
├── requirements.txt       # Dépendances
├── README.md              # Ce fichier
└── runs/detect/expX       # Dossier auto-généré avec les images détectées
```

---

## 🧪 Exemple

![screenshot](assets/example_detection.png)

---

## 🛠 Problèmes fréquents

- **Tkinter introuvable ?** : Sur certaines distributions Linux, il peut être nécessaire d’installer Tkinter avec :
  ```bash
  sudo apt install python3-tk
  ```

- **Pas de GPU ?** : YOLOv5 fonctionne également en CPU, mais peut être plus lent.

---

## 📌 Crédits

- YOLOv5 par [Ultralytics](https://github.com/ultralytics/yolov5)
- Interface développée en Tkinter
- Projet réalisé dans le cadre du Master 2 GLSI / SRT – 2025

---

## 🧠 Bonus : pour désactiver l’environnement virtuel

```bash
deactivate
```

---

## 📜 Licence

Ce projet est distribué sous la licence MIT.
```