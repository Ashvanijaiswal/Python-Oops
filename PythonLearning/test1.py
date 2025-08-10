import requests
from bs4 import BeautifulSoup
def fetch_stock_brief(symbol):
    try:
        # Add headers to mimic browser request
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        page = requests.get(f"https://finance.yahoo.com/quote/{symbol}", headers=headers)

        # Add status check
        if page.status_code != 200:
            print(f"Failed to retrieve data. Status code: {page.status_code}")
            return

        soup = BeautifulSoup(page.content, 'html.parser')

        # Safer element access
        price_element = soup.find("fin-streamer", {"data-field": "regularMarketPrice"})
        print(f"Price: {price_element.text}" if price_element else "Price data unavailable")

        # Alternative rating source
        rating_element = soup.find("div", {"data-test": "recommendation-mean"})
        print(f"Rating: {rating_element.text}" if rating_element else "Rating unavailable")

    except Exception as e:
        print(f"Error: {str(e)}")

fetch_stock_brief("OLA")