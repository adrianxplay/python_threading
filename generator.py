import csv

with open('numbers.csv', 'w') as file:
    for i in range(100000000):
        file.write("{},".format(i))

    file.close()