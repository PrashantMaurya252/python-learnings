chai_order=dict(type="Masala Chai",size="Large",sugar=2)
print(f"Chai Order : {chai_order}")

chai_recipe = {}
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"
print(f"Recipe Base : {chai_recipe['base']}")
print(f"Chai Recipe : {chai_recipe}")
del chai_recipe["liquid"]
print(f"chai recipe : {chai_recipe}")

print(f"Is sugar in chai_order ? : {"sugar" in chai_order}")

print(f"Chai Order Keys : {chai_order.keys()}")
print(f"Chai Order Values : {chai_order.values()}")
print(f"Chai Order Items : {chai_order.items()}")


last_item = chai_order.popitem()
print(f"Last Item : {last_item}")

extra_spices = {"cardamom":"crushed","ginger":"sliced"}
chai_order.update(extra_spices)
print(f"Updated Chai Order : {chai_order}")

customer_note = chai_order.get("size","No Note Present")
print(f"Customer Note : {customer_note}")