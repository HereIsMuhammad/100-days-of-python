"""
Day 83: HTTP Basics & Web Framework Concepts
Demonstrates making raw HTTP requests with `requests`
and inspecting the response — status code, headers, and body.
"""

import requests


def inspect_http_response(url: str):
    response = requests.get(url, timeout=10)

    print(f"URL: {url}")
    print(f"Status Code: {response.status_code}")
    print(f"Reason: {response.reason}")
    print("Headers:")
    for key, value in list(response.headers.items())[:5]:
        print(f"   {key}: {value}")

    print("\nBody (first 200 chars):")
    print(response.text[:200])


def demonstrate_methods():
    # A public test API that echoes back whatever you send it
    base = "https://httpbin.org"

    get_resp = requests.get(f"{base}/get", params={"lang": "python"})
    print("GET status:", get_resp.status_code)

    post_resp = requests.post(f"{base}/post", json={"name": "Ali", "day": 83})
    print("POST status:", post_resp.status_code)
    print("POST echoed data:", post_resp.json().get("json"))


if __name__ == "__main__":
    inspect_http_response("https://example.com")
    print("\n" + "-" * 50 + "\n")
    try:
        demonstrate_methods()
    except requests.RequestException as e:
        print(f"Network error: {e}")
