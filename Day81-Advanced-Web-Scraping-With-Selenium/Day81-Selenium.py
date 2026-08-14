"""
Day 81: Advanced Web Scraping with Selenium
Requires: pip install selenium  (and a Chrome browser installed)
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def scrape_with_selenium(url: str):
    options = Options()
    options.add_argument("--headless=new")   # run without opening a visible window
    options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get(url)

        # Wait up to 10 seconds for the <h1> to actually appear on the page
        heading = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "h1"))
        )

        print("Page title:", driver.title)
        print("Main heading:", heading.text)

        links = driver.find_elements(By.TAG_NAME, "a")
        print(f"Found {len(links)} links on the page")
        for link in links[:5]:
            print(" -", link.get_attribute("href"))

    finally:
        driver.quit()  # always close the browser, even if something fails


if __name__ == "__main__":
    scrape_with_selenium("https://example.com")
