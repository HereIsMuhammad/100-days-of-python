# Day 72: Working with APIs (requests module)

## Concept
APIs (Application Programming Interfaces) allow us to fetch data from the internet.  
Python’s `requests` module makes it easy to send HTTP requests and handle responses.

## What is an API?
- A way for programs to communicate  
- Provides structured data (usually JSON)  
- Example: Weather API, Public users API  

## Steps to Use an API
1. Import `requests` module  
2. Send a GET/POST request  
3. Receive response (JSON/Text)  
4. Extract required data  

## requests Module Functions
- `requests.get(url)` → Fetch data from URL  
- `requests.post(url, data)` → Send data  
- `response.status_code` → Check success  
- `response.json()` → Parse JSON data  

## Mini-Code Concept
- Fetch data from a public API  
- Display some fields  

## Use Cases
- Weather apps  
- Stock market data  
- Social media analysis  
- Automations and bots  

## Why Learn APIs?
- Almost all real-world apps use APIs  
- Required for Data Analysis, Automation, Web Development  
- Fetch live data dynamically