# Day 73: Virtual Environments & pip
# Note: Virtual environments are created outside Python code via terminal

# Mini-code demonstration of using a package inside venv

# 1. After creating venv and activating it
# pip install requests

import requests

# Example: Fetch random joke from API
url = "https://official-joke-api.appspot.com/random_joke"
response = requests.get(url)

if response.status_code == 200:
    joke = response.json()
    print("Here's a random joke for you:")
    print(joke['setup'])
    print(joke['punchline'])
else:
    print("Failed to fetch joke")