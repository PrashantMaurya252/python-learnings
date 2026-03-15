ingredients = ["water","black_tea","milk"]
ingredients.append("sugar")
print(f"Ingredients : {ingredients}")
ingredients.remove("water")
print(f"Ingredients : {ingredients}")


spice_options = ["ginger","cardamom"]
chai_ingredients = ["milk","water"]
spice_options.extend(chai_ingredients)
print(f"Spice Options : {spice_options}")
spice_options.insert(2,"black_tea")
print(f"Spice Options : {spice_options}")
last_added=spice_options.pop()
print(f"Last Added: {last_added}")
print(f"Spice Options : {spice_options}")
spice_options.reverse()
print(f"Reverse Spice Otions: {spice_options}")
spice_options.sort()
print(f"Sorted Spice Options : {spice_options}")

sugar_levels = [1,2,3,4,5]
print(f"Max Sugar Levels : {max(sugar_levels)}")
print(f"Min Sugar Levels : {min(sugar_levels)}")

strong_brew = ["water","black_tea"] * 3
print(f"strong_brew : {strong_brew}")