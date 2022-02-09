# -*- coding: UTF-8 -*-
from multiprocessing import Queue,Process
# 生产者
def producer(q,name,food):
  for i in range(3):
    print(f'{name}生产了{food}{i}')
    res = f'{food}{i}'
    q.put(res)
# 消费者
def consumer(q,name):
  while True:
    res = q.get(timeout=5)
    print(f'{name}吃了{res}')
if __name__ == '__main__':
  q = Queue() # 为的是让生产者和消费者使用同一个队列，使用同一个队列进行通讯
  p1 = Process(target=producer,args=(q,'Cecilia陈','巧克力'))
  c1 = Process(target=consumer,args=(q,'Tom'))
  p1.start()
  c1.start()