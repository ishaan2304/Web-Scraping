import requests
from bs4 import BeautifulSoup
import csv

url = "http://books.toscrape.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"
}
response = requests.get(url, headers=headers)
if response.status_code == 200:
    print("✅ Successfully fetched the webpage!")
else:
    print(f"❌ Failed to fetch the page. Status Code: {response.status_code}")

soup = BeautifulSoup(response.text, "html.parser")
books = soup.find_all("article", class_="product_pod")

# List to store book data
book_data = []

for book in books:
    # Extract book title
    title = book.h3.a["title"]

    # Extract price
    price = book.find("p", class_="price_color").text

    # Extract rating
    rating_class = book.p["class"]
    rating = rating_class[1]  # Second class name (e.g., "Three", "Four")

    # Append book data to the list
    book_data.append([title, price, rating])

    print(f"📖 Title: {title}")
    print(f"💰 Price: {price}")
    print(f"⭐ Rating: {rating}")
    print("-" * 50)

# Write data to CSV file
with open('books.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Price", "Rating"])
    writer.writerows(book_data)

print("✅ Data has been written to books.csv")
