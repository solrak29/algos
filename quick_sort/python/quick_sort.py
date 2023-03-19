import pdb
import secrets
import random
from typing import List
"""
    Quick Sort implementation.
"""
DEBUG = False
def breakpoint():
    if DEBUG:
        pdb.set_trace()

def _basic_partition(data_list: List, pivot: int, start: int, end: int) -> int:
    """
        This function is the basic partition that uses aux space
    """
    print(f'processing array {data_list[start:end]}')
    aux = [None] * (len(data_list))
    low = start
    high = end - 1
    pivot_value = data_list[pivot]
    breakpoint()
    for idx in range(start, end):
        print(f'processing {idx}')
        print(f'low {low} high {high}')
        if idx == pivot:
            continue
        if data_list[idx] > pivot_value:
            print(f'Adding at {high} for {idx}')
            aux[high] = data_list[idx]
            high -= 1
        else:
            print(f'Adding at {low} for {idx}')
            aux[low] = data_list[idx]
            low += 1
    aux[low] = pivot_value
    print(f'aux array {aux}')
    for idx in range(start, end):
        data_list[idx] = aux[idx]
    print(f'data list {data_list}')
    return low


def _lomoto_partition(data_list: List, pivot: int, start: int, end: int) -> int:

    pivot_value = data_list[pivot]
    #  Move the pivot value to the beginning
    breakpoint()
    if pivot != start:
        tmp = data_list[start]
        data_list[start] = pivot_value
        data_list[pivot] = tmp

    low_idx = start
    for high_idx in range(start + 1, end):
        print(f'idx => {high_idx}')
        if data_list[high_idx] < pivot_value:
            low_idx += 1 
            if high_idx > low_idx:
                tmp = data_list[low_idx]
                data_list[low_idx] = data_list[high_idx]
                data_list[high_idx] = tmp

    tmp = data_list[low_idx]
    data_list[low_idx] = data_list[start]
    data_list[start] = tmp
    print(f'end partition {data_list}')
    return low_idx


def _hoars_partition(data_list: List, pivot: int, start: int, end: int) -> int:
    breakpoint()
    pivot_value = data_list[pivot]
    if pivot != start:
        tmp = data_list[start]
        data_list[start] = pivot_value
        data_list[pivot] = tmp

    low_idx = start + 1
    high_idx = end - 1

    while low_idx <= high_idx:
        if data_list[low_idx] < pivot_value:
            low_idx += 1
        elif data_list[high_idx] > pivot_value:
            high_idx -= 1
        else:
            tmp = data_list[low_idx]
            data_list[low_idx] = data_list[high_idx]
            data_list[high_idx] = tmp

    #  the pointers have crossed so high_idx is used
    tmp = data_list[high_idx]
    data_list[high_idx] = data_list[start]
    data_list[start] = tmp

    return high_idx


# 
#  Comment or place accordingly to use any partition method
#
fn = _basic_partition
fn = _lomoto_partition
fn = _hoars_partition

Int_List = List[int]

def quick_sort(data_list: Int_List) -> Int_List:

    _helper(data_list, 0, len(data_list))
    return data_list


def _helper( data_list: Int_List, start: int, end: int):

    print(f'helper list {data_list} start {start} end {end}')
    if start >= end:
        return

    print(f'new size end-start {end-start} start {start} end {end}')
    pivot = secrets.choice([i for i in range(start,end)]) # maybe over kill, but the strongest generator
    print(f'pivot idx {pivot}')
    partition  = fn(data_list, pivot, start, end)
    print(f'sending left {start} to {partition}')
    _helper(data_list, start, partition)
    print(f'sending right {partition + 1} to {end}')
    _helper(data_list, partition + 1, end)



if __name__ == "__main__":
    list_to_sort = [4,2,8,7]
    print(f'Sorting array {list_to_sort}')
    sorted_list = quick_sort(list_to_sort)
    print('sorted')
    print(sorted_list)

    list_to_sort = [4,2,8,7,1,3,5,6]
    print(f'Sorting array {list_to_sort}')
    sorted_list = quick_sort(list_to_sort)
    print('sorted')
    print(sorted_list)

    list_to_sort = [3,2,1,4]
    print(f'sorting {list_to_sort}')
    sorted_list = quick_sort(list_to_sort)
    print('sorted')
    print(sorted_list)

    #
    #  Start using random samples to create bigger data sets to test
    #
    list_to_sort = random.sample(range(1,51), 50)
    print(f'sorting {list_to_sort}')
    sorted_list = quick_sort(list_to_sort)
    print('sorted')
    print(sorted_list)

    list_to_sort = random.sample(range(1,1001), 1000)
    print(f'sorting {list_to_sort}')
    sorted_list = quick_sort(list_to_sort)
    print('sorted')
    print(sorted_list)



