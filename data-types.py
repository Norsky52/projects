
product_name = "Widgits"
price_text = "9.99"
quantity = "60"
tax_rate_text ="0.10"

price = float(price_text)
quantity = int(quantity)
tax_rate =float(tax_rate_text)

subtotal = price * quantity
tax = subtotal * tax_rate
total = subtotal + tax

print(f"product:{product_name}")
print(f"price: ${price} * {quantity}")
print(f"subtotal: ${subtotal: .2f}")
print(f"tax: ({tax_rate * 100}%): ${tax:.2f}")
print(f"Total: ${total:.2f}")

