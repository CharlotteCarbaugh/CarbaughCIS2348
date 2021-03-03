#Carbaugh, Student ID 1815532
import datetime

file_name = input()
file = open(file_name)
content = file.readlines()
file.close()

new_date = ''
formated_dates = []

temp_date = []
new_date = ""
date_list = []

for date in content[0:-1]:
    new_date = date[0:-1]
    formated_dates.append(new_date)


months = {'January' : 1, 'Feburary': 2, 'March': 3, 'April': 4, 'May': 5,
          'June': 6, 'July': 7, 'August': 8, 'September': 9, 'October': 10,
          'November': 11, 'December': 12}



for date in formated_dates:
    temp_date = date.split(',')
    temp_date = date.split(' ')
    if temp_date[0] not in months:
        break
    elif len(temp_date) < 3:
        break
    else:
        if temp_date[1] > datetime.datetime:
            break
        if temp_date[3]> datetime.date.year:
            break
        else:
            print(temp_date)




print(formated_dates)
