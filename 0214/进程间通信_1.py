# -*- coding: UTF-8 -*-
from multiprocessing import Process
from time import sleep
from multiprocessing import Queue



def sub_task(content, q):
    counter = q.get();

    while counter < 8:
        print(content, flush=True)
        counter += 1
        q.put(counter)
        sleep(0.01)
        counter = q.get()



def main():
    q = Queue()
    q.put(0)
    p1 = Process(target=sub_task, args=('Ping', q))
    p1.start()

    p2 = Process(target=sub_task, args=('Pong', q))
    p2.start()
    while p1.is_alive() and p2.is_alive():
        pass
    q.put(8)

if __name__ == '__main__':
    main()