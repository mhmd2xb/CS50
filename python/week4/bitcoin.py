import sys
import requests

API_KEY = "YOUR_API_KEY_HERE"


def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        bitcoin = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    url = "https://rest.coincap.io/v3/assets/bitcoin"

    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.RequestException:
        sys.exit("Error retrieving Bitcoin price")

    try:
        data = response.json()
        price = float(data["data"]["priceUsd"])
    except (ValueError, KeyError, TypeError):
        sys.exit("Error parsing Bitcoin price")

    total = bitcoin * price

    print(f"${total:,.4f}")


main()
