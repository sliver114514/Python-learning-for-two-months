# 升级防呆版bmi计算器
BATES = {
    "USD": 1.00,
    "EUR": 0.94,
    "JPY": 149.85,
    "GBP": 0.85,
    "AUD": 1.56,
    "CNY": 6.75,
}

print("--- Current Converter ---")
print("Available currencies: USD,EUR,JPY,GBP,AUD,CNY")

while True:
    from_currency = input("Enter the currency to convert from:").strip().upper()

    if from_currency == "":
        print("Input cannot be empty.Please enter a currency code.")
        continue

    if from_currency not in BATES:
        print("Invalid currency. Please choose from USD,EUR,JPY,GBP,AUD,CNY.")
        continue

    break

while True:
    to_currency = input("Enter the currency to convert to:").strip().upper()
    if to_currency == "":
        print("Input cannot be empty.Please enter a currency code.")
        continue

    if to_currency not in BATES:
        print("Invalid currency. Please choose from USD,EUR,JPY,GBP,AUD,CNY.")
        continue

    if to_currency == from_currency:
        print("Source and target currencies cannot be same.Please choose a different target.")
        continue

    break

while True:
    try:
        amount_str = input("Enter the amount to convert:").strip()

        if amount_str == "":
            print("Amount cannot be empty.Please enter a number.")

        amount = float(amount_str)

        if amount <= 0:
            print("Amount must be greater than zero.Please enter a positive number.")
            continue

        break

    except ValueError:
        print("Invalid input. Please enter a numeric amount (e.g., 100 or 50.75).")
        continue

amount_in_usd = amount / BATES[from_currency]
converted_amount = amount_in_usd * BATES[to_currency]

print(f"\n {amount}{from_currency} is equal to {converted_amount:.2f}{to_currency}.")