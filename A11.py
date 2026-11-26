
Prices = {
    "Laptop": 50000,
    "Mouse": 500,
    "Keyboard": 1200,
    "Monitor": 10000,
    "Headphones": 2000
}

out_of_stock = {"Mouse", "Headphones"}

Order = ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones"]

total = 0

for item in Order:
    if item in out_of_stock:
        print(item, "is unavailable")
    else:
        total += Prices[item]
        print(item, "added to order")

print("\nFinal order value: Rs.", total)
