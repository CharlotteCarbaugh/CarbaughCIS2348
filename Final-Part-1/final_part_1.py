# Charlotte Carbaugh, ID #1815532
import csv

# starting files
file_holder = []
name_holder = []
name = ''

# Loop to get file names and contents from input
input_letter = input("Enter file name or n to quit")

while input_letter != 'n':
    name_holder.append(input_letter)
    name = input_letter + '.' + 'csv'
    with open(name, 'r') as csvfile:
        contents = csv.reader(name, delimiter = ',')

        rownum = 1
        for row in contents:
           file_holder.append(row)
           rownum += 1
    input_letter = input("Enter file name or n to quit")

print(file_holder)

# and here I got stuck and ran out of time