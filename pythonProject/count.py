import os
import csv

ranking_column_name = 'Name'
ranking_column_count = 'Count'
file_name = 'favorite_restaurant.csv'

class write(object):
    def __init__(self, rst):
        self.rst = rst


    def ranking(self):

        if os.path.exists(file_name):
            write.append_new_rst(self)

            # with open(file_name, 'r+') as csv_file:
            #     reader = csv.DictReader(csv_file)
                # for row in reader:
                    # if self.rst == row['Name']:
                    #     row_count = int(row['Count'])
                    #     row_count += 1
                    #     write.append_new_rst(self)
                    # else:
                    #     write.append_new_rst(self) #なぜ引数にセルフ？

        else:
            write.make_new_file(self)


    def make_new_file(self):

        with open(file_name, 'w', newline='') as csv_file:
            fieldnames = ['Name', 'Count']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({'Name': self.rst, 'Count': 1})

    def append_new_rst(self):
        with open(file_name, 'a') as csv_file:
            fieldnames = ['Name', 'Count']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writerow({'Name': self.rst, 'Count': 1})
