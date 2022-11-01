import os
import csv
import string
import termcolor
import count

colord = termcolor.colored
grn = 'green'
file_name = 'favorite_restaurant.csv'
# cnt = count.write()


class reccomend(object):
    def reccomending(self):
        with open('text_template/reccomend.txt', encoding="utf-8") as r:
            if os.path.exists(file_name):
                with open(file_name, 'r+', newline='') as csv_file:
                    reader = csv.DictReader(csv_file)
                    rec = string.Template(r.read())
                    for row in reader:
                        r_contents = rec.substitute(restaurant = row['Name'])
                        answer = input(colord(r_contents, grn))
                        new_answer = answer.capitalize()
                        # if new_answer == Yes:
                        #     # cnt.count_same_item(new_answer)
                        # elif new_answer == Y:
                        #     cnt.count_same_item(new_answer)

