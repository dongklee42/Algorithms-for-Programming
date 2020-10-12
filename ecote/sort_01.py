# 삽입정렬 예제
arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(arr)):	# 두 번째 인덱스 부터 탐색
	for j in range(i, 0, -1):	# 인덱스 i부터 0 까지 거꾸로 감소하며 탐색
		if arr[j] < arr[j - 1]:
			arr[j], arr[j - 1] =  arr[j - 1], arr[j]
		else:
			break
print(arr)
