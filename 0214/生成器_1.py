# -*- coding: UTF-8 -*-
def fib(max):
    a, b = 0, 1
    for _ in range(max):
        a, b = b, a+b
        yield a

obj = fib(10)
print(obj)
for v in obj:
    print(v)