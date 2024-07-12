import sqlite3
import json

conn = sqlite3.connect('db.sqlite3')


with open('data.json', 'r') as json_file:
    data = json.load(json_file)


for item in data:
    title = item["title"]
    author = item["author"]
    price = item["price"]

    conn.execute("INSERT INTO 'book_book' (title, author, price) VALUES (?, ?, ?)", 
                 (title, author,price )) 


conn.commit()
conn.close()        