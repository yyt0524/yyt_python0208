# -*- coding: UTF-8 -*-
def calc_avg():
    total, count = 0, 0
    avg = None
    while True:
        c_value = yield avg
        total += c_value
        count += 1
        avg = total / count

def main():
    obj = calc_avg()

    obj.send(None)
    for _ in range(5):
        print(obj.send(float(input())))

if __name__ == '__main__':
    main()