# 퀵정렬 예제
arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(arr, start, end):
	if start >= end:			# 원소가 1개인 경우 종료
		return
	
	#그렇지 않으면 pivot의 최초값을 start 포인트로
	pivot = start
	left = start + 1
	right = end
	
	# pivot이 엇갈릴 때 까지 반복
	while (left <= right):
		# 피벗보다 큰 데이터를 찾을 때 까지 반복
		while (left <= end and arr[left] <= arr[pivot]):
			left += 1
		# 피벗보다 작은 데이터를 찾을 때 까지 반복
		while (right > start and arr[right] >= arr[pivot]):
			right -= 1

		# 피봇이 엇갈렸다면
		if (left > right):		# 작은 데이터와 피벗 교체
			arr[right], arr[pivot] = arr[pivot], arr[right]
		else:					# 큰 데이터와 피벗 교체
			arr[left], arr[right] = arr[right], arr[left]
		
		# 분할 이후 좌우 각각 정렬 수행(재귀 반복)
		quick_sort(arr, start, (right - 1))
		quick_sort(arr, (right + 1), end)

quick_sort(arr, 0, (len(arr) - 1))

print(arr)