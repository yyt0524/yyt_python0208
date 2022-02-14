# -*- coding: UTF-8 -*-
import random
import time
from concurrent.futures import ThreadPoolExecutor
from threading import Thread

def download(*, filename):
    start = time.time()
    print(f'开始下载 {filename}.')
    time.sleep(random.randint(3, 6))
    print(f'{filename} 下载完成.')
    end = time.time()
    print(f'下载耗时: {end - start:.3f}秒.')

def main():
    with ThreadPoolExecutor(max_workers=4) as pool:
        filenames = [
            'file1.pdf',
            'file2.mp4',
            'file3.avi',
            'file4.word',
        ]
        start = time.time()
        for filename in filenames:
            pool.submit(download, filename=filename)
    end = time.time()
    print(f'总耗时: {end - start:.3f}秒.')
if __name__ == '__main__':
    main()