def clean_customer_name(name):
    return name.strip().title()


customer_name = "  faiz khan  "
print(clean_customer_name(customer_name))