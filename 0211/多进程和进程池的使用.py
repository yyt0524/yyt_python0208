# -*- coding: UTF-8 -*-
"""
  多进程和进程池的使用
  多线程因为GIL的存在不能够发挥CPU的多核特性
  对于计算密集型任务应该考虑使用多进程
  time python3 example22.py
  real    0m11.512s
  user    0m39.319s
  sys     0m0.169s
  使用多进程后实际执行时间为11.512秒，而用户时间39.319秒约为实际执行时间的4倍
  这就证明我们的程序通过多进程使用了CPU的多核特性，而且这台计算机配置了4核的CPU
  """
import concurrent.futures
import math

PRIMES = [
             1116281,
             1297337,
             104395303,
             472882027,
             533000389,
             817504243,
             982451653,
             112272535095293,
             112582705942171,
             112272535095293,
             115280095190773,
             115797848077099,
             1099726899285419
         ] * 5


def is_prime(n):
    """判断素数"""
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


def main():
    """主函数"""
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print('%d is prime: %s' % (number, prime))


if __name__ == '__main__':
    main()


'''

> **重点**：**多线程和多进程的比较**。
  >
  > 以下情况需要使用多线程：
  >
  > 1. 程序需要维护许多共享的状态（尤其是可变状态），
        Python中的列表、字典、集合都是线程安全的，所以使用线程而不是进程维护共享状态的代价相对较小。
  > 2. 程序会花费大量时间在I/O操作上，没有太多并行计算的需求且不需占用太多的内存。
  >
  > 以下情况需要使用多进程：
  >
  > 1. 程序执行计算密集型任务（如：字节码操作、数据处理、科学计算）。
  > 2. 程序的输入可以并行的分成块，并且可以将运算结果合并。
  > 3. 程序在内存使用方面没有任何限制且不强依赖于I/O操作（如：读写文件、套接字等）

'''