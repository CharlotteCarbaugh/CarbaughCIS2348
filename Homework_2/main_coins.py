#Carbaugh, Student ID #1815532
#Also, test 4 and 5 on Zybooks for 7.25 works when entered in Pycharm but not the book.


if __name__ == '__main__':

    inputval = int(input())

    def exact_change(user_total):
        if user_total == 0:
            print("no change")

        change = user_total

        numdollars = change // 100
        change %= 100

        numquarters = change // 25
        change = change % 25

        numdimes = change // 10
        change = change % 10

        numnickels = change // 5
        change = change % 5

        numpennies = change

        if numdollars != 0:
            if numdollars == 1:
                print(numdollars, "dollar")
            else:
                print(numdollars, "dollars")
        if numquarters != 0:
            if numquarters == 1:
                print(numquarters, "quarter")
            else:
                print(numquarters, "quarters")
        if numdimes != 0:
            if numdimes == 1:
                print(numdimes, "dime")
            else:
                print(numdimes, "dimes")
        if numnickels != 0:
            if numnickels == 1:
                print(numnickels, "nickel")
            else:
                print(numnickels, "nickels")
            if numpennies != 0:
                if numpennies == 1:
                    print(numpennies, "penny")
                else:
                    print(numpennies, "pennies")
    numpennies = exact_change(inputval)

