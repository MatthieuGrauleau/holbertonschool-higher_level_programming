#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_list = set()
    for num in my_list:
        uniq_list.add(num)
    total = sum(uniq_list)
    return (total)
