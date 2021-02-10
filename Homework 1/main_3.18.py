#Charlotte Carbaugh, Student ID 1815532
import math

height = int(input("Enter wall height (feet):\n"))
width = int(input("Enter wall width (feet):\n"))
wall_area = height*width
print("Wall area:", wall_area, "square feet")

gallon_paint = 350
paint_needed = wall_area/gallon_paint
paint_can = math.ceil(paint_needed)
print("Paint needed:",'{:.2f}'.format(paint_needed), "gallons")
print("Cans needed:", paint_can, "can(s)\n")

color_dic = {'red': 35, 'blue':25, 'green': 23}

color = str(input("Choose a color to paint the wall:\n"))

print("Cost of purchasing", color, "paint: $" + str(color_dic[color]*paint_can))