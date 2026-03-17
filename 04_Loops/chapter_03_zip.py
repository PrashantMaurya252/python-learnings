names = ["Hitesh","Meera","Sam","Ali"]
bills = [100,200,600,20]
for name,amount in zip(names,bills):
    print(f"{name} paid {amount} rupees")