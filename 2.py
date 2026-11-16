import csv
data = [
    ["Товар", "Цена за штуку", "Количество"],
    ["Тетрадь", 2.50, 4],
    ["Ручка", 1.20, 3],
    ["Папка", 4.00, 2],
    ["Маркер", 3.30, 1],
]
with open("purchases.csv", "w", encoding="utf-8-sig", newline="") as f:
  writer = csv.writer(f, delimiter=";")
  writer.writerows(data)
total = 0
with open("purchases.csv", "r", encoding="utf-8-sig") as f:
  reader = csv.reader(f, delimiter=";")
  next(reader)
  for row in reader:
    name = row[0]
    price = float(row[1])
    count = int(row[2])
    cost = price * count
    total += cost
    print(name, "- цена:", price, "кол-во:", count, "сумма:", round(cost, 2))
print()
print("Итого:", round(total, 2))
