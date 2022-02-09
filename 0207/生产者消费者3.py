# -*- coding: UTF-8 -*-
from multiprocessing import Queue, Process, JoinableQueue
import time, random


def producer(q, name, food):
    for i in range(3):
        print(f'{name}生产了{food}{i}')
        # time.sleep((random.randint(1,3)))
        res = f'{food}{i}'
        q.put(res)
    # q.put(None) # 当生产者结束生产的的时候，我们再队列的最后再做一个表示，告诉消费者，生产者已经不生产了，让消费者不要再去队列里拿东西了
    q.join()


def consumer(q, name):
    while True:
        res = q.get(timeout=5)
        # if res == None:break # 判断队列拿出的是不是生产者放的结束生产的标识，如果是则不取，直接退出，结束程序
        # time.sleep((random.randint(1, 3)))
        print(f'{name}吃了{res}')
        q.task_done()  # 向q.join()发送一次信号,证明一个数据已经被取走了


if __name__ == '__main__':
    q = JoinableQueue()  # 为的是让生产者和消费者使用同一个队列，使用同一个队列进行通讯
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

    # 把生产者设为守护进程
    c1.daemon = True
    c2.daemon = True
    # 告诉操作系统启动消费者进程
    c1.start()
    c2.start()

    p1.join()
    p2.join()
    p3.join()  # 等待生产者生产完毕

    print('主进程')

    ### 分析
    # 生产者生产完毕--这是主进程最后一行代码结束--q.join()消费者已经取干净了,没有存在的意义了
    # 这是主进程最后一行代码结束,消费者已经取干净了,没有存在的意义了.守护进程的概念.