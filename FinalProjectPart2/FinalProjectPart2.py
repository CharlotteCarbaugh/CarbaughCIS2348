# Charlotte Carbaugh
# Student ID #1815532
import datetime
# These functions are from Part 1 because the same things need to be done
# Format the inputs into something more usable


def format_file(dirty_list):
    # turn the input into a list of lists containing all the values
    # each inner-list is one entry from the original file
    iteration = 0
    i = 0

    # first split the input list apart by newlines to get the different entries
    clean_list = dirty_list.split('\n')

    # split these lines into lists, one for each original entry, and
    for item in clean_list:
        temp_list = item.split(",")
        # getting rid of the empty space/newline
        if temp_list == ['']:
            break
        # creates a list from the broken-apart string 'item'
        clean_list[iteration] = temp_list
        iteration += 1
    # further getting rid of empty items within the list
    for thingy in clean_list:
        if thingy == [''] or thingy == '':
            clean_list.pop(i)
        i += 1

    return clean_list


def make_dictionary(list_to_be_formatted):
    # creates a dictionary from a list for later use
    temp_dict = {}

    # turn list into dictionary
    for item in list_to_be_formatted:
        temp_dict[item[0]] = item

    return temp_dict


# Start of new functions (sans main)
def input_manager(mani_dict, service_dict, price_dict):
    # getting the initial input
    input_str = input("Please enter the manufacturer and item type, or q to quit\n")
    while input_str != 'q':
        # cleaning the input up
        input_list = input_str.split()
        for item in input_list:
            item.lower()
            item.rstrip()
            item.lstrip()

        # Part i: checking if the item exists
        exists = inventory_checker(input_list, mani_dict)

        # Part ii and iii, here because if the first part fails there's no reason going farther
        if exists != []:
            # part ii: find the most expensive item
            most_exp = your_item(exists, mani_dict, service_dict, price_dict)
            # part iii: recommend item
            also_rec(most_exp, mani_dict, service_dict, price_dict)

        input_str = input("Please enter the manufacturer and item type, or q to quit\n")


# Part i: Checks if the item is in the inventory
def inventory_checker(input_list, mani_dict):
    key_list = []
    # first check if the item is in the dictionary at all. Assuming the Manufacturer List has all items
    for key in mani_dict:
        manu = mani_dict[key][1].lower().rstrip()
        item_type = mani_dict[key][2].lower().rstrip()
        mani_in = False
        type_in = False
        for word in input_list:
            if word == manu:
                mani_in = True
            elif word == item_type:
                type_in = True
            else:
                continue
        # if item exists, add to list of valid items
        if mani_in == True and type_in == True:
            key_list.append(key)
            continue
    # else, return that no such item exists
    if key_list == []:
        print("No such item in inventory")
    return key_list


# Part ii: Returns a valid item or the most expensive valid item
def your_item(key_list, mani_dict, service_dict, price_dict):
    today_date = datetime.date.today()
    list_of_service_keys = service_dict.keys()
    list_of_item_keys = mani_dict.keys()
    viable_key = []

    # Testing to see if the key is in the service dictionary to prevent later Key Errors
    service_bool = False
    for key_list_key in key_list:
        bad_item = False
        # print(key_list_key)

        # testing if key is in service dictionary
        for key_test in list_of_service_keys:
            if key_list_key == key_test:
                service_bool = True

        # testing if the item is past service date
        if service_bool == True:
            for key_price in list_of_service_keys:
                if key_price == key_list_key:
                    key_date = service_dict[key_price][1]
                    test_date = key_date.split('/')
                    if datetime.date(int(test_date[2]), int(test_date[0]), int(test_date[1])) < today_date:
                        bad_item = True

        # testing if the item is damaged
        for key_item in list_of_item_keys:
            if key_item == key_list_key:
                if mani_dict[key_list_key][3] == "damaged":
                    bad_item = True
                    # print("howdy")

        # test if item code is viable, if so append to list for later checks
        if bad_item == False:
            # print("hi")
            viable_key.append(key_list_key)
        else:
            continue

    # finding the best key, or if none exist, setting it to zero
    if len(viable_key) == 0:
        best_key = 0
    else:
        best_key = viable_key[0]
        for good_key in viable_key:
            if good_key > best_key:
                best_key = good_key

    # I know this isn't in the prompt, but I need some error checking
    if best_key == 0:
        print("No item available")
    # Else print the best key info
    else:
        print("Your item is: " +
              ((str(best_key)).rstrip().lstrip() + " " +
               (str(mani_dict[best_key][1])).rstrip().lstrip() + " " +
               (str(mani_dict[best_key][2])).rstrip().lstrip() + " " +
               (str(price_dict[best_key][1])).rstrip().lstrip()))
    return best_key


# Part iii: recommend similar items
def also_rec(most_exp, mani_dict, service_dict, price_dic):
    today_date = datetime.date.today()

    # creating our usual list of keys
    list_of_keys = []
    for key in mani_dict.keys():
        list_of_keys.append(key)

    # making sure it won't recommend itself
    i = 0
    for key in list_of_keys:
        if key == most_exp:
            list_of_keys.pop(i)
        i += 1

    # elements of most expensive key for later cmparison
    most_exp_key_mani = mani_dict[most_exp][1]
    most_exp_key_type = mani_dict[most_exp][2]
    most_exp_key_price = price_dic[most_exp][1]

    # print(most_exp_key_mani, most_exp_key_type, most_exp_key_price)

    # narrowing down keys to the ones that meet the requirements in terms of manufacturer, damage, and type
    similar_key_list = []
    for key in list_of_keys:
        if mani_dict[key][3] == "damaged":
            continue
        elif str(mani_dict[key][2]) != most_exp_key_type:
            continue
        elif str(mani_dict[key][1]) == most_exp_key_mani:
            continue
        else:
            similar_key_list.append(key)

    # print(similar_key_list)
    # now to see if the rec keys are out of service
    i = 0
    service_key_list = service_dict.keys()
    for service_key in service_key_list:
        for test_key in similar_key_list:
            if int(service_dict[service_key][0]) == int(test_key):
                service_date = service_dict[test_key][1].split("/")
                # print(service_date)
                if datetime.date(int(service_date[2]), int(service_date[0]), int(service_date[1])) < today_date:
                    similar_key_list.pop(i)
            i += 1
        i = 0

    # print(similar_key_list)
    # now to check for the 'closes' in price
    good_rec = 0
    if len(similar_key_list) != 0:
        good_rec = similar_key_list[0]
        for key in similar_key_list:
            if (int(price_dic[key][1]) - int(most_exp_key_price)) < (int(price_dic[good_rec][1])
                                                                     - int(most_exp_key_price)):
                good_rec = key
    # print(good_rec)
    if good_rec != 0:
        print("You may, also, consider:", good_rec, mani_dict[good_rec][1], mani_dict[good_rec][2],
              price_dic[good_rec][1])


def main():
    # Using the code from Part 1 because the needed functions are the same
    # Getting the info from the files
    # Open the three files and save them to lists
    mani_list = open('ManufacturerList.csv')
    price_list = open('PriceList.csv')
    service_list = open('ServiceDatesList.csv')

    # read the files content into a container
    mani_content = mani_list.read()
    price_content = price_list.read()
    service_content = service_list.read()

    # Close the files to prevent memory leak
    mani_list.close()
    price_list.close()
    service_list.close()

    # cleaning up the files for later use
    mani_clean = format_file(mani_content)
    price_clean = format_file(price_content)
    service_clean = format_file(service_content)

    # make dictionaries from the clean lists for other functions
    mani_dict = make_dictionary(mani_clean)
    price_dict = make_dictionary(price_clean)
    service_dict = make_dictionary(service_clean)

    # start of new code
    # Get the input from the user in a cleaner way with all the data passed
    input_manager(mani_dict, service_dict, price_dict)


if __name__ == "__main__":
    main()
