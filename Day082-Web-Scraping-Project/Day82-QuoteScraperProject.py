"""
Day 82: Web Scraping Project — Quote Scraper & Exporter
Scrapes all quote pages from quotes.toscrape.com and saves results
to both CSV and JSON.
Requires: pip install requests beautifulsoup4
"""

import csv
import json
import time

import requests
from bs4 import BeautifulSoup

BASE_URL = "http://quotes.toscrape.com/page/{}/"
HEADERS = {"User-Agent": "Mozilla/5.0 (educational scraping demo)"}


def fetch_page(page_number: int):
    url = BASE_URL.format(page_number)
    response = requests.get(url, headers=HEADERS, timeout=10)
    response.raise_for_status()
    return response.text


def parse_quotes(html: str):
    soup = BeautifulSoup(html, "html.parser")
    quote_blocks = soup.find_all("div", class_="quote")

    quotes = []
    for block in quote_blocks:
        quotes.append({
            "text": block.find("span", class_="text").text.strip(),
            "author": block.find("small", class_="author").text.strip(),
            "tags": ", ".join(tag.text for tag in block.find_all("a", class_="tag")),
        })
    return quotes


def scrape_all_pages(max_pages: int = 3):
    all_quotes = []
    for page in range(1, max_pages + 1):
        try:
            html = fetch_page(page)
        except requests.RequestException as e:
            print(f"Stopping — network error on page {page}: {e}")
            break

        page_quotes = parse_quotes(html)
        if not page_quotes:
            print(f"No more quotes found after page {page - 1}, stopping.")
            break

        all_quotes.extend(page_quotes)
        print(f"Scraped page {page}: {len(page_quotes)} quotes")
        time.sleep(1)  # be polite — don't hammer the server

    return all_quotes


def save_to_csv(quotes, filename="quotes.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["text", "author", "tags"])
        writer.writeheader()
        writer.writerows(quotes)
    print(f"Saved {len(quotes)} quotes to {filename}")


def save_to_json(quotes, filename="quotes.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(quotes, f, indent=2, ensure_ascii=False)
    print(f"Saved {len(quotes)} quotes to {filename}")


if __name__ == "__main__":
    quotes = scrape_all_pages(max_pages=3)
    if quotes:
        save_to_csv(quotes)
        save_to_json(quotes)
