# -*- coding: UTF-8 -*-
from multiprocessing import Queue, Process
import time, random


def producer(q, name, food):
    for i in range(3):
        print(f'{name}生产了{food}{i}')
        time.sleep((random.randint(1, 3)))
        res = f'{food}{i}'
        q.put(res)
    # q.put(None) # 当生产者结束生产的的时候，我们再队列的最后再做一个表示，告诉消费者，生产者已经不生产了，让消费者不要再去队列里拿东西了


def consumer(q, name):
    while True:
        res = q.get(timeout=5)
        if res == None: break  # 判断队列拿出的是不是生产者放的结束生产的标识，如果是则不取，直接退出，结束程序
        time.sleep((random.randint(1, 3)))
        print(f'{name}吃了{res}')


if __name__ == '__main__':
    q = Queue()  # 为的是让生产者和消费者使用同一个队列，使用同一个队列进行通讯
    # 多个生产者进程
    p1 = Process(target=producer, args=(q, 'Cecilia陈', '巧克力'))
    p2 = Process(target=producer, args=(q, 'xichen', '冰激凌'))
    p3 = Process(target=producer, args=(q, '喜陈', '可乐'))
    # 多个消费者进程
    c1 = Process(target=consumer, args=(q, 'Tom'))
    c2 = Process(target=consumer, args=(q, 'jack'))

    # 告诉操作系统启动生产者进程
    p1.start()
    p2.start()
    p3.start()

    # 告诉操作系统启动消费者进程
    c1.start()
    c2.start()

    p1.join()
    p2.join()
    p3.join()

    q.put(None)  # 几个消费者put几次
    q.put(None)