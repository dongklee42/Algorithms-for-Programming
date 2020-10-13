# 퀵정렬 예제를 파이썬에서 효율적으로 작성하기
arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(arr):
	if len(arr) <= 1:
		return arr
	
	pivot = arr[0]		# 첫번째 원소를 피벗으로
	tail = arr[1 : ]	# 피벗을 제외한 리스트

	left_side = [x for x in tail if x <= pivot]
	right_side = [y for y in tail if y > pivot]

	return (quick_sort(left_side) + [pivot] + quick_sort(right_side))

print(quick_sort(arr))
