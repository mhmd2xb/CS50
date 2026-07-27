import os
import sys
import requests


def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    api_key = os.environ.get("COINCAP_API_KEY")
    if not api_key:
        sys.exit("Set the COINCAP_API_KEY environment variable")

    try:
        bitcoin = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    url = "https://rest.coincap.io/v3/assets/bitcoin"

    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.RequestException:
        sys.exit("Error retrieving Bitcoin price")

    data = response.json()

    price = float(data["data"]["priceUsd"])

    total = bitcoin * price

    print(f"${total:,.4f}")


main()
