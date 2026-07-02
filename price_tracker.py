import requests

url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"

print("Fetching Bitcoin live price")

response = requests.get(url)
data = response.json()

required_data = data["price"]

live_price = round(float(required_data) , 2)

print("-------------------------")
print(f'Live price of Bitcoin is ${live_price}')
print("-------------------------")