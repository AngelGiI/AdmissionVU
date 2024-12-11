# -*- coding: utf-8 -*-
"""
Created on Sat May 21 21:35:15 2022

@author: Angel
"""

def merge(left, right, pos):
    if len(left) == 0:
        return right
    if len(right) == 0:
        return left
    result = []
    index_left = index_right = 0
    while len(result) < len(left) + len(right):
        if left[index_left][pos] <= right[index_right][pos]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1
        if index_right == len(right):
            result += left[index_left:]
            break
        if index_left == len(left):
            result += right[index_right:]
            break
    return result

def merge_sort(array,pos):
    if len(array) < 2:
        return array
    midpoint = len(array) // 2
    return merge(
        left=merge_sort(array[:midpoint],pos),
        right=merge_sort(array[midpoint:],pos),
        pos=pos)