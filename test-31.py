import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import csv
from googlesearch import search
import requests
from bs4 import BeautifulSoup

# Fonction pour effectuer le web scraping d'un URL donné
def scrape_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.title.string.strip().replace('\n', ' ').replace(',', '')
    paragraphs = [p.get_text().strip().replace('\n', ' ').replace(',', '') for p in soup.find_all('p')]
    return title, paragraphs

# Fonction pour ajouter un mot-clé à la liste
def add_keyword():
    keyword = keyword_entry.get()
    if keyword:
        keyword_listbox.insert(tk.END, keyword)
        keyword_entry.delete(0, tk.END)

# Fonction pour supprimer un mot-clé de la liste
def remove_keyword():
    selected_indices = keyword_listbox.curselection()
    if selected_indices:
        keyword_listbox.delete(selected_indices)

# Fonction pour effectuer le web scraping des mots-clés et enregistrer les données dans un fichier CSV
def scrape_keywords():
    keywords = keyword_listbox.get(0, tk.END)
    if not keywords:
        messagebox.showinfo('Aucun mot-clé', 'Veuillez ajouter des mots-clés.')
        return
    
    filename = 'scraped_data.csv'
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Mot-clé', 'URL', 'Titre', 'Contenu (balise p)'])
        
        for keyword in keywords:
            try:
                for url in search(keyword, num_results=4, lang='fr'):
                    title, paragraphs = scrape_url(url)
                    for paragraph in paragraphs:
                        writer.writerow([keyword, url.replace('\n', ' ').replace(',', ''), title, paragraph])
            except Exception as e:
                messagebox.showinfo('Erreur', f'Une erreur est survenue lors du web scraping pour le mot-clé "{keyword}": {str(e)}')

    messagebox.showinfo('Terminé', f'Les données ont été enregistrées dans le fichier "{filename}".')

# Création de la fenêtre principale
window = tk.Tk()
window.title('Web Scraping avec Beautiful Soup')
window.geometry('400x400')

# Cadre pour les mots-clés
keyword_frame = ttk.LabelFrame(window, text='Mots-clés')
keyword_frame.pack(pady=10)

# Liste des mots-clés
keyword_listbox = tk.Listbox(keyword_frame, width=30)
keyword_listbox.pack(padx=10, pady=5)

# Cadre pour l'ajout de mots-clés
add_keyword_frame = ttk.Frame(keyword_frame)
add_keyword_frame.pack(pady=5)

keyword_label = ttk.Label(add_keyword_frame, text='Mot-clé:')
keyword_label.pack(side=tk.LEFT)

keyword_entry = ttk.Entry(add_keyword_frame, width=20)
keyword_entry.pack(side=tk.LEFT)

add_button = ttk.Button(add_keyword_frame, text='Ajouter', command=add_keyword)
add_button.pack(side=tk.LEFT, padx=5)

# Bouton pour supprimer un mot-clé
remove_button = ttk.Button(keyword_frame, text='Supprimer', command=remove_keyword)
remove_button.pack(pady=5)

# Bouton pour lancer le web scraping
scrape_button = ttk.Button(window, text='Web Scraping', command=scrape_keywords)
scrape_button.pack(pady=10)

# Lancement de la boucle principale
window.mainloop()