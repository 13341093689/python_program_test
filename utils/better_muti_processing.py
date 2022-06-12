from multiprocessing import Queue,Process,Pool

import time
import os

def func(n,output_queue):
    start = time.time()

    print(n, time.time())
    count=0
    for i in range(10000000) :
        output_queue.put(i)
        count+= i
    stop = time.time()
    print(n, stop-start)

if __name__ == '__main__':
    start = time.time()
    output = Queue()
    print(os.cpu_count())
    thread_list = []
    for i in range(10):
        th = Process(target=func, args=(i,output))
        thread_list.append(th)
        th.start()

    for th_item in thread_list:
        while th_item.is_alive():
            while False == output.empty():
                output.get()

    for th_item in thread_list:
        th_item.join()

    print("主进程执行完毕!")