# Day 82: Web Scraping Project

## Project: Quote Scraper & Exporter
Combines Days 80-81 skills into one small real project:
1. Scrape quotes from a practice site (`requests` + `BeautifulSoup`).
2. Clean and structure the data.
3. Save results to both **CSV** and **JSON** (recall Days 64-65).
4. Handle errors gracefully (network issues, missing elements).

## Project Structure
```
scraper/
├── scraper.py       # scraping logic
├── quotes.csv        # output
└── quotes.json        # output
```

## Design Decisions
- Separate **scraping** (getting data) from **exporting** (saving data) into
  different functions — easier to test and reuse.
- Use `try/except` around network calls (Day 33: Exception Handling).
- Respect the target site: add delays between page requests, set a
  descriptive `User-Agent`.

## Key Takeaways
- Real-world scripts combine multiple skills: HTTP requests, HTML parsing,
  file I/O, and error handling.
- Always validate scraped data before saving — websites change structure
  and can break your scraper silently.
- Consider pagination: many sites split data across multiple pages
  (`?page=2`, "Next" buttons, etc.).

## Next Steps (Ideas to Extend)
- Add command-line arguments (`argparse`) to choose the export format.
- Schedule the scraper to run daily and track price/data changes over time.
- Store results in the SQLite database from Day 66 instead of flat files.
