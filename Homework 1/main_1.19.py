#Charlotte Carbaugh, Student ID 1815532

lemon_juice = float(input("Enter amount of lemon juice (in cups):\n"))
water = float(input("Enter amount of water (in cups):\n"))
agave_nectar = float(input("Enter amount of agave nectar (in cups):\n"))
servings = int(input("How many servings does this make?\n"))
print("")

print("Lemonade ingredients - yields",'{:.2f}'.format(servings), "servings")
print('{:.2f}'.format(lemon_juice), "cup(s) lemon juice")
print('{:.2f}'.format(water), "cup(s) water")
print('{:.2f}'.format(agave_nectar), "cup(s) agave nectar\n")

wanted_servings = float(input("How many servings would you like to make?\n"))
print("")

parts_per_lemon = lemon_juice/servings
parts_per_water = water/servings
parts_per_agave = agave_nectar/servings

print("Lemonade ingredients - yields",'{:.2f}'.format(wanted_servings), "servings")
print('{:.2f}'.format(parts_per_lemon*wanted_servings), "cup(s) lemon juice")
print('{:.2f}'.format(parts_per_water*wanted_servings), "cup(s) water")
print('{:.2f}'.format(parts_per_agave*wanted_servings), "cup(s) agave nectar\n")

lemon_gallons = (parts_per_lemon * wanted_servings) / 16
water_gallons = (parts_per_water * wanted_servings) / 16
agave_gallons = (parts_per_agave * wanted_servings) / 16


print('Lemonade ingredients - yields','{:.2f}'.format(wanted_servings), "servings")
print('{:.2f}'.format(lemon_gallons), "gallon(s) lemon juice")
print('{:.2f}'.format(water_gallons), "gallon(s) water")
print('{:.2f}'.format(agave_gallons), "gallon(s) agave nectar")