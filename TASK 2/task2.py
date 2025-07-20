# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2750,
    "MSFT": 330,
    "AMZN": 135
}

# Dictionary to hold user's stock portfolio
portfolio = {}

# Input: Number of different stocks
num_stocks = int(input("Enter number of different stocks you own: "))

# Get stock details from the user
for _ in range(num_stocks):
    stock_name = input("Enter stock symbol (e.g., AAPL, TSLA): ").upper()
    quantity = int(input(f"Enter quantity of {stock_name}: "))
    
    if stock_name in stock_prices:
        portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity
    else:
        print(f"Warning: {stock_name} not found in price list. Skipping.")

# Calculate total investment
total_value = 0
print("\nYour Portfolio Summary:")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = price * qty
    total_value += value
    print(f"{stock}: {qty} shares × ${price} = ${value}")

print(f"\nTotal Investment Value: ${total_value}")

# Optional: Save to file
save_option = input("Do you want to save this summary to a file? (yes/no): ").lower()

if save_option == 'yes':
    filename = input("Enter filename (with .txt or .csv): ")
    with open(filename, 'w') as file:
        file.write("Stock,Quantity,Price,Value\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            value = price * qty
            file.write(f"{stock},{qty},{price},{value}\n")
        file.write(f"\nTotal Investment Value: ${total_value}")
    print(f"Portfolio saved to {filename}")
