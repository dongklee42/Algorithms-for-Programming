# 파이썬의 이진탐색 라이브러리 활용
from bisect import bisect_left, bisect_right

arr = [1, 2, 4, 4, 8]
target = 4

print(bisect_left(arr, target))
print(bisect_right(arr, target))
