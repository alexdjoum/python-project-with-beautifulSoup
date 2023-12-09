import webbrowser
import requests
from bs4 import BeautifulSoup
from tkinter import Tk, Label, Entry, Button, messagebox

# Fonction pour effectuer le web scraping des résultats de recherche
def web_scraping(url, label):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            # Utiliser les méthodes de BeautifulSoup pour extraire les informations pertinentes des pages web
            # Ici, je stocke le résultat dans un fichier.
            print(soup)
        else:
            label.config(text="Veuillez activer votre connexion", fg="red")
    except requests.exceptions.RequestException as e:
        label.config(text="Veuillez activer votre connexion", fg="red")

# Fonction appelée lorsque le bouton "Ajouter au dictionnaire" est cliqué
def ajouter_mot_cle():
    mot_cle = entry.get()  # Récupère le mot clé du champ d'entrée
    if mot_cle:
        dictionnaire.append(mot_cle)  # Ajoute le mot clé au dictionnaire
        print("Le contenu du dictionnaire ==> ", dictionnaire)
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

        # Créer un Label pour afficher le statut
        label = Label(window, text="")
        label.pack(pady= 10)

        # Effectue le web scraping des résultats de recherche
        web_scraping(url, label)

        # Affiche le nombre de résultats de recherche dans le label
        label.config(text=f"Nombre de résultats pour '{mot_cle}': {get_number_of_results(url)}")
        label.configure(fg="green")

    messagebox.showinfo("Web scraping terminé", "Le web scraping des résultats de recherche est terminé.")

# Fonction pour obtenir le nombre de résultats de recherche pour un URL donné
def get_number_of_results(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}
    result = requests.get(url, headers=headers)    

    soup = BeautifulSoup(result.content, 'html.parser')

    total_results_text = soup.find("div", {"id": "result-stats"}) #.find(text=True, recursive=False) # this will give you the outer text which is like 'About 1,410,000,000 results'
    results_num = total_results_text.text # now will clean it up and remove all the characters that are not a number .
    return results_num 
    print(results_num)

    


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


import requests


