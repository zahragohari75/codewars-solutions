# 8 kyu - Sum without highest and lowest number
# https://www.codewars.com/kata/576b93db1129fcf2200001e6

def sum_array(arr):
    if not arr or len(arr) < 3 :
        return 0
    
    total = sum(arr)
    return sum(arr) - min(arr) - max(arr)
