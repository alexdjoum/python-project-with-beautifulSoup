import webbrowser
import requests
from bs4 import BeautifulSoup
from tkinter import Tk, Label, Entry, Button, messagebox

# Fonction pour effectuer le web scraping des résultats de recherche
def web_scraping(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup)
    # utiliser les méthodes de BeautifulSoup pour extraire les informations pertinentes des pages web
    # ici je stoke le resultat dans un fichier.

# Fonction appelée lorsque le bouton "Ajouter au dictionnaire" est cliqué
def ajouter_mot_cle():
    mot_cle = entry.get()  # Récupère le mot clé du champ d'entrée
    if mot_cle:
        dictionnaire.append(mot_cle)  # Ajoute le mot clé au dictionnaire
        entry.delete(0, 'end')  # Efface le contenu du champ d'entrée
    else:
        messagebox.showwarning("Champ vide", "Veuillez entrer un mot clé.")

# Fonction appelée lorsque le bouton "Soumettre" est cliqué
def soumettre_recherche():
    if not dictionnaire:
        messagebox.showwarning("Dictionnaire vide", "Veuillez ajouter des mots clés au dictionnaire.")
        return

    for mot_cle in dictionnaire:
        url = "https://www.google.com/search?q=" + mot_cle

        # Effectue le web scraping des résultats de recherche
        web_scraping(url)

    messagebox.showinfo("Web scraping terminé", "Le web scraping des résultats de recherche est terminé.")

    # Ouvre le fichier contenant les résultats
    #webbrowser.open("resultats.txt")

# Crée la fenêtre principale
window = Tk()

# Crée le champ d'entrée
entry = Entry(window, width=64)
entry.pack(pady=10)

# Crée le bouton "Ajouter au dictionnaire"
bouton_ajouter = Button(window, text="Ajouter au dictionnaire", command=ajouter_mot_cle, width=55)
bouton_ajouter.pack(pady=10)

# Crée le bouton "Soumettre"
bouton_soumettre = Button(window, text="Soumettre", command=soumettre_recherche, width=55)
bouton_soumettre.pack()

# Initialise le dictionnaire
dictionnaire = []

# Lance la boucle principale de l'interface
window.mainloop()