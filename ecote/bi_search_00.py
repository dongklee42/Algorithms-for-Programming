# 재귀함수로 구현하는 이진 탐색
def binary_search(arr, target, start, end):
	if start > end:
		return None
	
	mid = (start + end) // 2

	if arr[mid] == target:
		return mid
	elif arr[mid] > target:
		return binary_search(arr, target, start, (mid - 1))
	else:
		return binary_search(arr, target, mid + 1, end)

# 데이터 받기
n, target = list(map(int, input().split()))
arr = list(map(int, input().split()))

# 결과 출력
result = binary_search(arr, target, 0, (n - 1))

if result == None:
	print("원소가 존재하지 않습니다.")
else:
	print(result + 1)