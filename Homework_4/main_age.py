# Charlotte Carbaugh, Student ID 1815532
def main():
    str_list = []
    temp_word = ''
    splitter = []
    temp_split = []
    correct_word = ''

# Input the list
    while temp_word != '-1':
        temp_word = input()
        if temp_word == '-1':
            break
        str_list.append(temp_word)

    for line in str_list:
        temp_word = line
        temp_split = temp_word.split()
        try:
            if temp_split[1].isnumeric() == False:
                raise ValueError
        except ValueError:
            temp_split[1] = '-1'

        temp_split[1] = str(int(temp_split[1]) + 1)
        correct_word = temp_split[0] + ' ' + temp_split[1]
        splitter.append(correct_word)

    for item in splitter:
        print(item)

if __name__ == "__main__":
    main()