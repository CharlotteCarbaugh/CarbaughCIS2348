#Carbaugh, Student ID 1815532
test_str = input().lower()
new_str = test_str.replace(" ", "")
y = 0

while y < len(new_str):
    if new_str[y] == new_str[-1-y]:
        y += 1
    else:
        print(test_str, "is not a palindrome")
        break

if y == len(new_str):
    print(test_str,"is a palindrome")
