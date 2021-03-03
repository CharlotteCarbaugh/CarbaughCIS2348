#Carbaugh, Student ID 1815532
import csv

file_name = input()

file = open(file_name)
content = file.read()
file.close()

content.strip()
new_list = content.split(",")

replace_word = ''
word_count  = 0
for word in new_list:
    if word.find("\n") > 0:
        replace_word = word[0:-1]
        new_list.pop(word_count)
        new_list.append(replace_word)
    word_count += 1

used_words = []
counter = 0

for word in new_list:
    if word not in used_words:
        word_times = new_list.count(word)
        used_words.append(word)
        print(word, word_times)
    counter += 1
