import csv, random
from datetime import datetime

products = [
    ("P1001","iPhone 15",79999),
    ("P1002","Samsung TV 55 inch",54999),
    ("P1003","Nike Shoes",2999),
    ("P1004","Dell Laptop",65999),
    ("P1005","Sony Headphones",4999),
]

with open("data/orders.csv","w",newline="") as f:
    w = csv.writer(f)
    w.writerow(["order_id","customer","product","price","date"])
    for i in range(1,21):
        p = random.choice(products)
        w.writerow([f"ORD{i}", f"Customer{i}", p[1], p[2], datetime.now().strftime("%Y-%m-%d")])

print("Done! 20 orders created")