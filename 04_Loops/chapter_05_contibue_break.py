flavours = ["Ginger","Out of Stock","Lemon","Discontinued","Tulsi"]

for flavour in flavours:
    if flavour == "Out of Stock":
        continue
    if flavour == "Discontinued":
        break
    print(f"{flavour} Item Found")

print("Outside of the loop")


staff = [("Amit",19),("Zara",16),("Raj",17)]
for name,age in staff:
    if(age >=18):
        print(f"{name} is eligible to manage the staff")
        break
else:
    print("No one is eligible to manage the staff")
        