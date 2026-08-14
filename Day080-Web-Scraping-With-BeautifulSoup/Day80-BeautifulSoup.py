"""
Day 80: Web Scraping with BeautifulSoup
Requires: pip install requests beautifulsoup4
"""

import requests
from bs4 import BeautifulSoup

HEADERS = {"User-Agent": "Mozilla/5.0 (educational scraping demo)"}


def scrape_quotes():
    """Scrapes quotes from the well-known scraping-practice site quotes.toscrape.com"""
    url = "http://quotes.toscrape.com/"
    response = requests.get(url, headers=HEADERS, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    quotes = soup.find_all("div", class_="quote")
    results = []

    for quote_block in quotes:
        text = quote_block.find("span", class_="text").text
        author = quote_block.find("small", class_="author").text
        tags = [tag.text for tag in quote_block.find_all("a", class_="tag")]
        results.append({"text": text, "author": author, "tags": tags})

    return results


if __name__ == "__main__":
    try:
        for q in scrape_quotes():
            print(f'"{q["text"]}" — {q["author"]}  (tags: {", ".join(q["tags"])})')
    except requests.RequestException as e:
        print(f"Network error while scraping: {e}")
