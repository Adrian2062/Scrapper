# git init
# git status -- if you want to check what are the status of files
# git diff -- if you want to check what are the changes
# git add . 
# git commit -m "Your message"
# copy paste git code from github
################
# 1. change the code
# 2. git add .
# 3. git commit -m "Your message"
# 4. git push
################
import json
import requests
from bs4 import BeautifulSoup
url = "https://books.toscrape.com/"

def scrape_book(url):
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to retrieve the page")
        return
    # Set encoding explicitly to handel special characters correctly
    response.encoding = response.apparent_encoding
    soup =  BeautifulSoup(response.text,"html.parser")
    all_books = []
    books = soup.find_all("article",class_ = "product_pod")
    for book in books:
        title = book.h3.a['title']
        price_text = book.find("p",class_ = 'price_color').text
        currency = price_text[0]
        price = float(price_text[1:])
        print(title,currency,price)
        all_books.append(
            {
                "title":title,
                "currency":currency,
                "price":price,
            }
        )
        return all_books
books = scrape_book(url)

with open("books.json","w",encoding='utf-8') as f:
    import json
    json.dump(books,f , indent=4, ensure_ascii=False)