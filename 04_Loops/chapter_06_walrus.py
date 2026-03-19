# value = 13
# remainder = value % 5
# if remainder:
#     print(f"Remainder is {remainder}")

value = 13
if(remainder := value % 5):
    print(f"Remainder is {remainder}")

available_size = ["small","medium","large"]
if(requested_size := input("Enter your Chai Cup Size : ")) in available_size:
    print(f"Serving {requested_size}")
else:
    print(f"Size Unavailable {requested_size}")