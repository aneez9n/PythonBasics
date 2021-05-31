

enter_weight = int(input("enter your weight.  "))
pound = enter_weight * 2.2046226218
kg = enter_weight / 2.2046
change_to = input("change to kilogram (KG) or Pound (P)   ")
if change_to == "kg   ":
    print(kg)
elif change_to == "p  ":
    print(pound)