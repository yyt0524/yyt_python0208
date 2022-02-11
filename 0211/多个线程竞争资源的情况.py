# -*- coding: UTF-8 -*-
"""
  多线程程序如果没有竞争资源处理起来通常也比较简单
  当多个线程竞争临界资源的时候如果缺乏必要的保护措施就会导致数据错乱
  说明：临界资源就是被多个线程竞争的资源
  """
import time
import threading

from concurrent.futures import ThreadPoolExecutor


class Account(object):
    """银行账户"""

    def __init__(self):
        self.balance = 0.0
        self.lock = threading.Lock()

    #存款
    def deposit(self, money):
        # 通过锁保护临界资源
        with self.lock:
            new_balance = self.balance + money
            time.sleep(0.001)
            self.balance = new_balance


def main():
    """主函数"""
    account = Account()
    # 创建线程池
    pool = ThreadPoolExecutor(max_workers=10)
    futures = []
    '''
    submit(fn, *args, **kwargs)：将 fn 函数提交给线程池。
                                *args 代表传给 fn 函数的参数，
                                *kwargs 代表以关键字参数的形式为 fn 函数传入参数
    '''
    for _ in range(50):
        future = pool.submit(account.deposit, 1)
        futures.append(future)
    # 关闭线程池
    pool.shutdown()
    for future in futures:
        future.result()
    print(account.balance)


if __name__ == '__main__':
    main()