import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
CSE_ID = os.getenv("CSE_ID")

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
}

def search_google(query, num_results=5):
    url = f"https://www.googleapis.com/customsearch/v1?q={query}&cx={CSE_ID}&key={API_KEY}&num={num_results}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return [(item["title"], item["link"]) for item in data.get("items", [])]
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return []

def get_price(url):
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        price_tags = soup.select("span.price, div.price, p.price, strong.price")
        prices = [float(tag.get_text(strip=True).replace("£", "").replace(",", "")) for tag in price_tags if tag.get_text(strip=True).replace("£", "").replace(",", "").replace(".", "").isdigit()]
        
        return min(prices) if prices else None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def apply_discount(price, soup):
    discount_tags = soup.select("span.promo-price, div.discount")
    if discount_tags:
        discount_text = discount_tags[0].get_text(strip=True).replace("£", "")
        try:
            discount = float(discount_text)
            price -= discount
        except ValueError:
            pass
    return price

def find_best_price(search_results):
    best_price = None
    best_url = None

    for title, url in search_results:
        price = get_price(url)
        if price is not None and (best_price is None or price < best_price):
            best_price = price
            best_url = url

    return best_url, best_price

query = "REGENOVUE DEEP PLUS LIDOCAINE 1,1ML best price site:.uk"
search_results = search_google(query)
best_site, best_price = find_best_price(search_results)

if best_price:
    print(f"Best price: £{best_price} at {best_site}")
else:
    print("No price found.")
