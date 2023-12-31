import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}
URL     = "https://www.google.com/search?q=programming"
result = requests.get(URL, headers=headers)    

soup = BeautifulSoup(result.content, 'html.parser')

total_results_text = soup.find("div", {"id": "result-stats"}) #.find(text=True, recursive=False) # this will give you the outer text which is like 'About 1,410,000,000 results'
results_num = total_results_text.text.split()[1] # now will clean it up and remove all the characters that are not a number .
print(results_num)