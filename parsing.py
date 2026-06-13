import requests
from bs4 import BeautifulSoup
import csv
base_url = "https://quotes.toscrape.com/"
response = requests.get(base_url)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    quotes = soup.find_all("div", class_="quote")
    with open('quote.csv', mode='w',encoding='utf-8',newline='') as file:
        writer = csv.writer(file)
        headers = ['Quote', 'Author']
        writer.writerow(headers)
        for quote in quotes:
            text = quote.find(class_='text').text
            author = quote.find(class_='author').text
            writer.writerow([text,author])
else:
    print("Error")


