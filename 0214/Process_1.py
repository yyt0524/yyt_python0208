# -*- coding: UTF-8 -*-
from multiprocessing import Process, current_process
from time import sleep

def sub_task(content, nums):
    # 通过current_process函数获取当前进程对象
    # 通过进程对象的pid和name属性获取进程的ID号和名字
    print(f'PID: {current_process().pid}')
    print(f'Name: {current_process().name}')

    # 通过下面的输出不难发现，每个进程都有自己的nums列表，进程之间本就不共享内存
    # 在创建子进程时复制了父进程的数据结构，三个进程从列表中pop(0)得到的值都是20
    counter, total = 0, nums.pop(0)
    print(f'Loop count: {total}')
    sleep(0.5)
    while counter<total:
        counter += 1
        print(f'{counter}: {content}')
        sleep(0.01)

def main():
    nums = [20, 30, 40]
    Process(target=sub_task, args=('YYYY_', nums)).start()
    Process(target=sub_task, args=('XXXX_', nums)).start()
    sub_task('Good', nums)

if __name__ == '__main__':
    main()