# Charlotte Carbaugh, student ID #1815532
import csv
import datetime


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


# Functions for creating the FullInventory file
def full_inventory(mani_dict, price_dict, service_dict):
    # set up the ultimate list from the three dictionaries
    grand_list = []

    # set up the list for the keys we need
    list_of_keys = []
    for key in mani_dict.keys():
        list_of_keys.append(key)

    # sort the keys by lowest item ID
    for i in range(len(list_of_keys)):
        index_largest = i
        for j in range(i, len(list_of_keys)):
            if mani_dict[list_of_keys[j]][1] < mani_dict[list_of_keys[index_largest]][1]:
                index_largest = j
            elif mani_dict[list_of_keys[j]][1] == mani_dict[list_of_keys[index_largest]][1]:
                if mani_dict[list_of_keys[j]][2] < mani_dict[list_of_keys[index_largest]][2]:
                    index_largest = j

        temp_key = list_of_keys[i]
        list_of_keys[i] = list_of_keys[index_largest]
        list_of_keys[index_largest] = temp_key

    # set up the sorted list needed for the full inventory file
    for key in list_of_keys:
        temp_list = [mani_dict[key][0], mani_dict[key][1], mani_dict[key][2], price_dict[key][1], service_dict[key][1],
                     mani_dict[key][3]]
        grand_list.append(temp_list)

    return grand_list


def full_inventory_file(full_inv_list):
    # create the full inventory file needed
    file = open('FullInventory.csv', 'w', newline='')
    with file:
        write = csv.writer(file)
        for row in full_inv_list:
            write.writerow(row)
        #   print(row)

    file.close()


# Functions for creating the various item-type files
def item_inventory_sorter(full_inventory_list):
    # set up the containers we need to organize the lists
    list_of_keys = []
    i = 0
    temp_list_entry = []
    dict_of_things = {}

    # set up a list of keys we need--in this case, the item type
    for item in full_inventory_list:
        list_of_keys.append(item[2])

    # set up the dictionary with the keys from before
    for key in list_of_keys:
        while i < len(full_inventory_list):
            if full_inventory_list[i][2] == key:
                # Since we don't need everything from every entry, this is a custom one with just what the client wants
                temp_list_items = [full_inventory_list[i][0], full_inventory_list[i][1], full_inventory_list[i][3],
                                   full_inventory_list[i][4], full_inventory_list[i][5]]
                temp_list_entry.append(temp_list_items)
            i += 1
        # customized dictionary with just the elements needed for this file, sorted by key
        dict_of_things[key] = temp_list_entry
        # clean the iterator/container for re-use
        temp_list_entry = []
        i = 0

    # now to sort the dictionary's keys into the order the client asked for
    for this_key in list_of_keys:
        index = dict_of_things[this_key]
        # sort index
        for i in range(len(index) - 1):
            lowest_letter = i
            for j in range(i + 1, len(index)):
                if int(index[j][0]) < int(index[lowest_letter][0]):
                    lowest_letter = j

            temp_key = index[i]
            index[i] = index[lowest_letter]
            index[lowest_letter] = temp_key

        dict_of_things[this_key] = index

    return dict_of_things


def item_inventory_file(inventory_dict):
    list_of_keys = []

    # create a key list
    for key in inventory_dict.keys():
        list_of_keys.append(key)

    # first iterate through the item types and create the files

    for key in list_of_keys:
        file_name = key.capitalize() + 'Inventory.csv'
        #    print(file_name)
        file = open(file_name, 'w', newline='')
        write = csv.writer(file)
        # now to create the files
        for list_row in inventory_dict[key]:
            write.writerow(list_row)

        file.close()


# Function for creating the PastServiceDateInventory file
def service_date_checker(grand_list):
    service_date_list = []
    today_date = datetime.date.today()
    organized_service_list = []

    # create a list of overdue dates
    for sub_list in grand_list:
        # creating a date so today_date and the entry date can be compared
        service_date = sub_list[4].split('/')
        # comparing the dates, if it's lesser (older), adding the date to the  list
        if datetime.date(int(service_date[2]), int(service_date[0]), int(service_date[1])) <= today_date:
            service_date_list.append(sub_list)
            organized_service_list.append([sub_list[0], datetime.date(int(service_date[2]), int(service_date[0]),
                                                                      int(service_date[1]))])

    # organizing the overdue dates from oldest to newest
    for i in range(len(organized_service_list) - 1):
        lowest_letter = i
        for j in range(i + 1, len(organized_service_list)):
            if organized_service_list[j][1] < organized_service_list[lowest_letter][1]:
                lowest_letter = j

        temp_key = organized_service_list[i]
        organized_service_list[i] = organized_service_list[lowest_letter]
        organized_service_list[lowest_letter] = temp_key

    # its easier to just create the file here, since the function has all the necessary lists
    file = open('PastServiceDateInventory.csv', 'w', newline='')
    write = csv.writer(file)
    with file:
        for service in organized_service_list:
            for sub_list in grand_list:
                if service[0] == sub_list[0]:
                    write.writerow(sub_list)

    file.close()


def damaged_inventory_report(grand_list):
    damaged_dict = {}

    # first find all the damaged items and put them in a dictionary
    for sub_list in grand_list:
        if sub_list[5] == 'damaged':
            damaged_dict[sub_list[0]] = sub_list

    # create a list of keys for damaged item dictionary
    list_of_keys = []
    for key in damaged_dict.keys():
        list_of_keys.append(key)

    # sort the keys by lowest item ID
    for i in range(len(list_of_keys)):
        index_largest = i
        for j in range(i, len(list_of_keys)):
            if int(damaged_dict[list_of_keys[j]][3]) > int(damaged_dict[list_of_keys[index_largest]][3]):
                index_largest = j

        temp_key = list_of_keys[i]
        list_of_keys[i] = list_of_keys[index_largest]
        list_of_keys[index_largest] = temp_key

    #    print(list_of_keys)
    #    print(damaged_dic)

    # as before, its easier to create the file here where all the data is
    file = open('DamagedInventory.csv', 'w', newline='')
    with file:
        write = csv.writer(file)
        for row in list_of_keys:
            final_row = [damaged_dict[row][0], damaged_dict[row][1], damaged_dict[row][2], damaged_dict[row][3],
                         damaged_dict[row][4]]
            write.writerow(final_row)
        # print(final_row)

    file.close()


def main():
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

    #    print(mani_clean)
    #    print(price_clean)
    #    print(service_clean)

    # make dictionaries from the clean lists for other functions
    mani_dict = make_dictionary(mani_clean)
    price_dict = make_dictionary(price_clean)
    service_dict = make_dictionary(service_clean)

    #   Creating the final containers to be passed to the file creation functions
    full_inventory_list = full_inventory(mani_dict, price_dict, service_dict)
    item_type_inventory = item_inventory_sorter(full_inventory_list)
    service_date_checker(full_inventory_list)
    damaged_inventory_report(full_inventory_list)

    # Creating the files from the processed containers
    # Note: on all the files, there's an odd error where the outputted file has '########' as an entry
    # If you click on the value, it will turn into the correct view. I have no idea what causes this or how to fix it.
    full_inventory_file(full_inventory_list)
    item_inventory_file(item_type_inventory)


if __name__ == "__main__":
    main()
