def print_order(name,chai_type):
    print(f"{name} ordered {chai_type}")


print_order("Prashant","Ginger")
print_order("Aman","Lemon")


def fetch_sales():
    print("printing sales data")

def filter_valid_sales():
    print("Filtering Valid sales")

def summerize_data():
    print("Summerizing Data")


def generateReport():
    fetch_sales()
    filter_valid_sales()
    summerize_data()
    print("Report is ready")

generateReport()