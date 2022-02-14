# -*- coding: UTF-8 -*-
import random
import time
from threading import Thread

class DownloadThread(Thread):
    def __init__(self, filename):
        self.filename = filename
        super().__init__()

    def run(self):
        start = time.time()
        print(f'开始下载 {self.filename}')
        time.sleep(random.randint(2,5))
        print(f'{self.filename} 下载完成')
        end = time.time()
        print(f'用时：{end - start:.3f}秒.')

def main():
    threds = [
        DownloadThread('file1.pdf'),
        DownloadThread('file2.pdf'),
        DownloadThread('file3.pdf'),
    ]
    start = time.time()
    for thred in threds:
        thred.start()

    for t in threds:
        t.join()

    end = time.time()
    print(f'总用时： {end-start:.3f}秒')

if __name__ == '__main__':
    main()