import csv
from collections import Counter

total = 0
count = 0
products = Counter()

with open("data/orders.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        total += int(row["price"])
        count += 1
        products[row["product"]] += 1

print(f"Total Orders: {count}")
print(f"Total Revenue: Rs {total}")
print("Top Products:")
for p, c in products.most_common():
    print(f"  {p} : {c} orders")