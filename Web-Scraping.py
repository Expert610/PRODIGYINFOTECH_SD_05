import requests
from bs4 import BeautifulSoup
import csv

# Set the URL
url = "https://books.toscrape.com/catalogue/page-1.html"

# Send a GET request with headers
headers = {
    "User-Agent": "Mozilla/5.0"
}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Find all product containers
products = soup.find_all("article", class_="product_pod")

# Prepare CSV file
with open("products.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Product Name", "Price", "Rating"])

    # Loop through products
    for product in products:
        name = product.h3.a["title"]
        price = product.find("p", class_="price_color").text.strip()
        rating_class = product.find("p", class_="star-rating")["class"]
        rating = rating_class[1]  # Second class is the rating (e.g., "Three")

        writer.writerow([name, price, rating])

print("Data saved to products.csv")
