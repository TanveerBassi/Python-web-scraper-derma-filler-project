# 💉 Derma Filler Price Scraper

📌 Description

This Python project helps you find the cheapest derma filler available online. Using Google Custom Search API and BeautifulSoup, it searches for the product, scrapes prices from multiple websites, and returns the lowest available price (including discounts).
⚙️ Features

✅ Searches Google for the best derma filler prices
✅ Scrapes websites for price information
✅ Extracts discount prices when available
✅ Returns the cheapest option that delivers to the UK
🛠️ Technologies Used

    🐍 Python
    🌍 Google Custom Search API
    🔍 BeautifulSoup (Web Scraping)
    🌐 Requests (HTTP Requests)
    🔒 dotenv (for API Key Security)

📌 Setup Instructions
1️⃣ Clone the Repository

git clone https://github.com/TanveerBassi/Python-web-scraper-derma-filler-project.git
cd Python-web-scraper-derma-filler-project

2️⃣ Install Dependencies

pip install -r requirements.txt

3️⃣ Secure Your API Keys

Create a .env file and add your Google API Key and Custom Search Engine ID:

API_KEY=your_google_api_key
CSE_ID=your_custom_search_engine_id

⚠️ Important: Do not share your .env file or API keys!
4️⃣ Run the Script

python scraper.py

📌 Example Output

Best price: £17.99 at https://aesthisave.co.uk/product/regenovue-deep-plus-1-1-ml-copy/

📌 Future Improvements

🚀 Support more countries 🌍
🚀 Add price history tracking 📊
🚀 Implement Telegram/email alerts 📩
📌 Contributions

Feel free to fork, modify, and submit a pull request if you have improvements!

📌 License

📝 MIT License – Free to use and modify.
