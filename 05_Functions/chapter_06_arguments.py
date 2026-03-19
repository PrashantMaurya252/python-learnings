def make_chai(tea,milk,sugar):
    print(tea,milk,sugar)

make_chai("Dargeeling","Yes","Low")  #positional
make_chai(tea="Green",milk="Yes",sugar="No")    #Keywords


def special_chai(*ingredients,**extras):
    print("Ingredients",ingredients)
    print("Extras",extras)



special_chai("Cinnamon","Cardomom",sweeter="Honey",foam="Yes")


chai_type = ["Kadak","Light","Kadak","Ginger"]

strong_chai = list(filter(lambda chai:chai != "Kadak",chai_type))
print(strong_chai)