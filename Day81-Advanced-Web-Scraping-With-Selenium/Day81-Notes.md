# Day 81: Advanced Web Scraping with Selenium

## Why Selenium?
`BeautifulSoup` only reads static HTML. Many modern sites load content
with JavaScript **after** the page loads (infinite scroll, buttons, login
forms). Selenium automates a real browser, so it can click, scroll, wait,
and see the fully-rendered page.

## Setup
```bash
pip install selenium
```
Modern Selenium (4.6+) can auto-manage the browser driver, so you usually
just need a browser like Chrome installed.

## Basic Usage
```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://example.com")

heading = driver.find_element(By.TAG_NAME, "h1")
print(heading.text)

driver.quit()
```

## Locating Elements
```python
driver.find_element(By.ID, "main-title")
driver.find_element(By.CLASS_NAME, "price")
driver.find_element(By.CSS_SELECTOR, "div.card > h2")
driver.find_elements(By.TAG_NAME, "a")   # plural -> list of all matches
```

## Interacting with the Page
```python
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("python tutorials")
search_box.submit()

button = driver.find_element(By.ID, "load-more")
button.click()
```

## Waiting for Content to Load
Never rely on fixed `time.sleep()` for reliability — use explicit waits:
```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "results"))
)
```

## Headless Mode (no visible browser window)
```python
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)
```

## BeautifulSoup vs Selenium
| | BeautifulSoup | Selenium |
|---|---|---|
| Speed | Fast | Slower (real browser) |
| JS-rendered content | ❌ | ✅ |
| Can click/type/scroll | ❌ | ✅ |
| Resource usage | Low | High |

## Summary
Use `requests` + `BeautifulSoup` for simple static pages, and Selenium when
you need to render JavaScript or interact with the page like a real user.
