# -*- coding: UTF-8 -*-

#简单选择排序
def select_sort(items, comp=lambda x, y: x < y):
    items = items[:]
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i+1, len(items)):
            if(comp(items[j], items[min_index])):
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
    return items

#冒泡排序
def bubble_sort(items, comp=lambda x, y : x>y):
    items = items[:]
    for i in range(len(items) - 1):
        swapped = False
        for j in range(len(items) - 1 -i):
            if comp(items[j], items[j+1]):
                items[j], items[j + 1] = items[j+1], items[j]
                swapped = True
        if not swapped:
            break
    return items

list = [1,5,7, 2, 3, 9, 8]
#list1 =  select_sort(list)
list1 =  bubble_sort(list)
print(list1)