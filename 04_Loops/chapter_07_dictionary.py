users = [
    {"id":1,"total":100,"coupon":"A20"},
    {"id":2,"total":150,"coupon":"P20"},
    {"id":3,"total":80,"coupon":"F20"}
]

discounts ={
    "A20":(0.2,0),
    "P20":(0.5,0),
    "F20":(0,10)
}

for user in users:
    percent,fixed = discounts.get(user["coupon"],(0,0))
    discount = user["total"] * percent +fixed
    print(f"user {user["id"]} paid {user["total"]} and get discount of {discount} rupees")