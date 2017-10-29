import csv
import time
start_time = time.time()

print("Loading data in main thread")

with open("numbers.csv", "r", newline="\n") as file:
    reader = csv.reader(file, lineterminator="\n", delimiter=",")
    numbers_list = list(reader)[0]

    result = 0

    print("Starting process")

    for i in numbers_list:
        if i is not '':
            result += int(i)

    print("Single thread results: {}".format(result))

print("--- %s seconds ---" % (time.time() - start_time))