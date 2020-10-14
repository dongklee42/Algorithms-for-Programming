# 값이 특정 범위에 속하는 데이터 개수 구하기
from bisect import bisect_left, bisect_right

def count_by_range(arr, left_val, right_val):
	left_idx = bisect_left(arr, left_val)
	right_idx = bisect_right(arr, right_val)
	return (right_idx - left_idx)

# 배열 선언
arr = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

# 값이 4인 데이터 개수 출력
print(count_by_range(arr, 4, 4))

# 값이 [-1, 3] 범위인 데이터 개수 출력
print(count_by_range(arr, -1, 3))
