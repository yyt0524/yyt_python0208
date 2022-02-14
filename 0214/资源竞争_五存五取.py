# -*- coding: UTF-8 -*-
import threading
import time

from concurrent.futures import ThreadPoolExecutor
from threading import RLock
from random import randint
from time import sleep

class Account(object):
    """银行账户"""

    def __init__(self):
        self.balance = 0.0
        rlock = RLock()
        self.condition = threading.Condition(rlock)

    def deposit(self, money):
        """存钱"""
        #获取锁
        with self.condition:
            new_balance = self.balance + money
            time.sleep(0.01)
            self.balance = new_balance
            self.condition.notify_all()

    def withdraw(self, money):
        with self.condition:
            while money>self.balance:
                self.condition.wait()
            new_balance = self.balance - money
            time.sleep(0.01)
            self.balance = new_balance

def add_money(account):
    while True:
        money = randint(5, 10)
        account.deposit(money)
        print(threading.current_thread().name,
              ':', money, '====>', account.balance)
        sleep(1)


def sub_money(account):
    while True:
        money = randint(10, 30)
        account.withdraw(money)
        print(threading.current_thread().name,
              ':', money, '<====', account.balance)
        sleep(1)


def main():
    """主函数"""
    account = Account()
    with ThreadPoolExecutor(max_workers=16) as pool:
        for _ in range(5):
            pool.submit(add_money, account)
        for _ in range(5):
            pool.submit(sub_money, account)



if __name__ == '__main__':
    main()

    """
      多个线程竞争一个资源 - 保护临界资源 - 锁（Lock/RLock）
      多个线程竞争多个资源（线程数>资源数） - 信号量（Semaphore）
      多个线程的调度 - 暂停线程执行/唤醒等待中的线程 - Condition
    """