def update_order():
    chai_type = "Elachi"
    def kitchen():
        nonlocal chai_type
        chai_type = "Kesar"
    kitchen()
    print(f"After Kitch update",chai_type)

update_order()