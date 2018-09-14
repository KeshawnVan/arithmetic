#!/usr/bin/env python
# -*- coding: utf-8 -*-


def search(source_list, target):
    left = 0
    right = len(source_list) - 1
    while left <= right:
        mid = (left + right) // 2
        mid_value = source_list[mid]
        if mid_value == target:
            return mid + 1
        if mid_value > target:
            right = mid - 1
        if mid_value < target:
            left = mid + 1
    return None


sorted_list = [1, 2, 4, 5, 67, 78, 88]
print(search(sorted_list, 67))
print(search(sorted_list, 11))
