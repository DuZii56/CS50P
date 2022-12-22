import requests
import sys

bitcoin_url = "https://api.coindesk.com/v1/bpi/currentprice.json"

def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    try:
        bitcoin_qty = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
    res = requests.get(bitcoin_url)
    requested_data = res.json()
    current_price = requested_data["bpi"]["USD"]["rate_float"]
    total = current_price * bitcoin_qty
    print(f"${total:,.4f}")

if __name__ == "__main__":
    main()
