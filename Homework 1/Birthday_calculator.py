#Charlotte Carbaugh, Student ID #1815532


print("Birthday Calculator\nCurrent Day")
current_month = int(input("Month:"))
current_day = int(input("Day:"))
current_year = int(input("Year:"))

print("Birthday")
bday_month = int(input("Month:"))
bday_day = int(input("Day:"))
bday_year = int(input("Year"))

age = current_year - bday_year

if bday_month >= current_month:
    if bday_day > current_day:
        age -= 1

print("You are",age,"years old.")