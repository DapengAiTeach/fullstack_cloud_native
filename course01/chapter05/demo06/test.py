import requests

# Test connection to API A
try:
    print("Sending request to API A...")
    resp = requests.get("http://api_a:8000")
    print(resp.text)
except Exception as e:
    print(f"Error: {e}")

# Test connection to API B
try:
    print("Sending request to API B...")
    resp = requests.get("http://api_b:8000")
    print(resp.text)
except Exception as e:
    print(f"Error: {e}")