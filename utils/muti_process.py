from multiprocessing import Queue,Process

import time

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
    thread_list = []
    for i in range(10):
        th = Process(target=func, args=(i,output))
        thread_list.append(th)
        th.start()
    for th_item in thread_list:
        th_item.join()

    print("主进程执行完毕!")