import tkinter as tk
import screen_brightness_control as sbc
import ctypes
import os

# Fonction pour ajuster la luminosité de l'écran
def ajuster_luminosite(valeur):
    sbc.set_brightness(valeur)  # Modifier la luminosité à 50%

# Fonction pour changer la police
def changer_police(taille):
    ctypes.windll.shcore.SetProcessDpiAwareness(1)  # Activer la haute DPI pour la police
    police = f"Helvetica {taille}"  # Définir la police en fonction de la valeur du scale
    root.option_add('*Font', police)  # Changer la police par défaut

# Créer une fenêtre tkinter
root = tk.Tk()
root.title("Contrôle Visuel")

# Boutons pour chaque fonctionnalité
scale_luminosite = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=ajuster_luminosite, width=55)
scale_luminosite.set(50)  # Valeur par défaut
scale_luminosite.pack()

# Label luminosité
label_police = tk.Label(root, text="Ajuster luminosité")
label_police.pack()

# Scale pour changer la police
scale_police = tk.Scale(root, from_=8, to=24, orient=tk.HORIZONTAL, command=changer_police, width=55)
scale_police.set(12)  # Taille de police par défaut
scale_police.pack()

# Label pour le scale de la police
label_police = tk.Label(root, text="Taille de la police")
label_police.pack()


# Lancer l'application
root.mainloop()
