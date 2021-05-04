# Charlotte Carbaugh, Student ID 1815532
def selection_sort_descend_trace(list):
    temp_word = ''
    for i in range(len(list) -1):
        index_largest = i
        for j in range(i + 1, len(list)):
            if list[j] > list[index_largest]:
                index_largest =  j

        temp_num = list[i]
        list[i] = list[index_largest]
        list[index_largest] = temp_num

        for k in list:
            temp_word += str(k) + ' '

        print(temp_word)
        temp_word = ''

def main():
    split_list = []
    temp_list = input()

    split_list = temp_list.split()

    iter = 0

    while iter < len(split_list):
        split_list[iter] = int(split_list[iter])
        iter += 1

    selection_sort_descend_trace(split_list)


if __name__ == "__main__":
    main()