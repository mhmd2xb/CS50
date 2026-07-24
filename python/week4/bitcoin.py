import sys
import requests

API_KEY = "271d4a289b22018bee2943cf45a428da1196b3133e901fc9b81caf977e9cc192"


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

    data = response.json()

    price = float(data["data"]["priceUsd"])

    total = bitcoin * price

    print(f"${total:,.4f}")


main()