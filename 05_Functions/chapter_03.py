def calculate_bill(cups,price_per_cup):
    return cups * price_per_cup

my_bill = calculate_bill(3,15)
print(my_bill)

print(f"Order for table 2: ",calculate_bill(2,50))

def add_vat(price,vat_value):
    return price*vat_value

orders = [100,200,300]

for price in orders:
    final_amount = add_vat(price,4)
    print(f"final amount : {final_amount}")