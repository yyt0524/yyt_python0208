# -*- coding: UTF-8 -*-
import time

from concurrent.futures import ThreadPoolExecutor
from threading import RLock

class Account(object):
    """银行账户"""

    def __init__(self):
        self.balance = 0.0
        self.rlock = RLock()
    def deposit(self, money):
        """存钱"""
        #获取锁
        self.rlock.acquire()
        try:
            new_balance = self.balance + money
            time.sleep(0.01)
            self.balance = new_balance
        finally:
            self.rlock.release()


def main():
    """主函数"""
    account = Account()
    with ThreadPoolExecutor(max_workers=16) as pool:
        for _ in range(100):
            pool.submit(account.deposit, 1)
    print(account.balance)


if __name__ == '__main__':
    main()