# Day 80: Web Scraping with BeautifulSoup

## What is Web Scraping?
Extracting data from web pages automatically instead of copy-pasting manually.
Always check a site's `robots.txt` and Terms of Service before scraping.

## Tools Needed
```bash
pip install requests beautifulsoup4
```
- `requests`: downloads the HTML of a page.
- `beautifulsoup4`: parses HTML and lets you search/navigate it.

## Basic Workflow
```python
import requests
from bs4 import BeautifulSoup

response = requests.get("https://example.com")
soup = BeautifulSoup(response.text, "html.parser")

print(soup.title.text)          # page title
print(soup.find("h1").text)     # first <h1>
```

## Finding Elements
```python
soup.find("div")                       # first matching tag
soup.find_all("a")                     # all matching tags -> list
soup.find("div", class_="price")       # by class
soup.find("span", id="main-price")     # by id
soup.select("div.card > h2")           # CSS selectors
```

## Extracting Data
```python
link = soup.find("a")
print(link.text)          # visible text
print(link["href"])       # attribute value

for item in soup.find_all("li", class_="product"):
    print(item.text.strip())
```

## Being a Good Scraper
- Add a `User-Agent` header and delays between requests (`time.sleep`).
- Handle errors — sites go down, structure changes.
- Prefer an official API if one exists; it's more reliable than scraping HTML.

## Summary
`requests` fetches raw HTML, `BeautifulSoup` turns it into a searchable tree.
Together they're the standard combo for simple, static-page scraping.
