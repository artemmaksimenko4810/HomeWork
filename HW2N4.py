n = int(input())

customers = {}

for i in range(n):
    customer, product, count = input().split()
    count = int(count)

    if customer not in customers:
        customers[customer] = {}

    if product in customers[customer]:
        customers[customer][product] += count

    else:
        customers[customer][product] = count

for customer in sorted(customers.keys()):
    print(f"{customer}:")

    for product in sorted(customers[customer].keys()):
        print(f"{product} {customers[customer][product]}")
