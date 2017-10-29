import csv
import threading
import time
start_time = time.time()

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]


def add_list(list):
    tmp = 0
    for i in list:
        if i is not '':
            tmp += int(i)

    results.append(tmp)


class MyThread(threading.Thread):
    def __init__(self, name, thread_id, data):
        threading.Thread.__init__(self)
        self.name = name
        self.id = thread_id
        self.data = data

    def run(self):
        print("Starting new thread: {} {}".format(self.id, self.name))
        # thread_lock.acquire()
        add_list(self.data)
        # thread_lock.release()
        print("End pricessing time of {}".format(self.name))


print("Waiting for the list lenght")
thread_lock = threading.Lock()
numbers_list = []
list_len = 0

with open("numbers.csv", "r", newline="\n") as file:
    reader = csv.reader(file, lineterminator="\n", delimiter=",")
    numbers_list = list(reader)[0]
    list_len = len(numbers_list)
    print("list lenght {}".format(list_len))

chunks_gen = chunks(numbers_list, 5000000)

print("writing tmp files...")

results = []
thread_queue = []
count = 0

for chunk in chunks_gen:
    array = list(chunk)

    thread_queue.append(MyThread("Thread_{}".format(count), count, array))
    count += 1
    # result_thread.start()
    # result_thread.join()

for t in thread_queue:
    t.run()

value = 0
for r in results:
    print(r)
    value += r

print("the result is: %i" % value)
print("--- %s seconds ---" % (time.time() - start_time))
