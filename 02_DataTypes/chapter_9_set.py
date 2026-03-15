essesntial_spices = {"Ginger","Cardamom","Cinemon"}
optional_spices={"Clover","Ginger","Black_Paper"}

all_spices = essesntial_spices | optional_spices
print(f"All Spices :",all_spices)
common_spices = essesntial_spices & optional_spices
print(f"Common Spices : {common_spices}")
only_in_essential = essesntial_spices - optional_spices
print(f"Only in Essential Spices",only_in_essential)