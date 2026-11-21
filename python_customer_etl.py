customers = [
    {"id": 1, "name": " faiz "},
    {"id": 2, "name": " rahul "}
]

for customer in customers:
    customer["name"] = customer["name"].strip().title()

print(customers)