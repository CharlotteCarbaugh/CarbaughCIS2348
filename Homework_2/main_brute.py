#Carbaugh, Student ID 1815532

first_var_x = int(input())
first_var_y = int(input())
first_var_ans = int(input())
second_var_x = int(input())
second_var_y = int(input())
second_var_ans = int(input())
isdone = False

for var_1 in range(-10, 11):
    for var_2 in range(-10, 11):
        if ((first_var_x*var_1) + (first_var_y*var_2) == first_var_ans) and\
                ((second_var_x*var_1) + (second_var_y*var_2) == second_var_ans):
            print(var_1, var_2)
            isdone = True
            break
    if (isdone == True):
        break


if isdone == False:
    print("No solution")