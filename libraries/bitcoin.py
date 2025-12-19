import sys
import requests

def main():
    # Check if the number of arguments is correct
    if len(sys.argv) != 2:
        print("Usage: python bitcoin.py <number of bitcoins>")
        sys.exit(1)

    try:
        # Convert the command-line argument to a float
        bitcoins = float(sys.argv[1])
    except ValueError:
        print("Error: The number of bitcoins must be a number.")
        sys.exit(1)

    try:
        # Fetch the current Bitcoin price from the CoinDesk API
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()  # Parse the JSON response
    except requests.RequestException:
        print("Error: Could not fetch Bitcoin price data.")
        sys.exit(1)

    # Extract the current price of Bitcoin in USD
    bitcoin_price = data['bpi']['USD']['rate_float']

    # Calculate the total cost for the specified amount of bitcoins
    total_cost = bitcoins * bitcoin_price

    # Output the total cost formatted to four decimal places
    print(f"${total_cost:,.4f}")

if __name__ == "__main__":
    main()
