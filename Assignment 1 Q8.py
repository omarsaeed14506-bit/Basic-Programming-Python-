cart = {
    "Laptop":25000,
    "Mouse":500,
    "Keyboard":1200,
    "Headphones":900
}
total = 0
count = 0
for item,price in cart.items():
    total += price
    if price > 1000:
        count += 1
    print(f"{item}: {price}")
if total > 25000:
    print("Expensive Order")
else:
    print("Normal Order")
print(f"Total: {total}, Count: {count}")
