# 계수정렬
arr = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

#모든 범위를 포함하는 리스트 선언(값은 0으로 초기화)
cnt = [0] * (max(arr) + 1)		# 0~9 중 그 안에 들어있는 가장 큰 숫자로

for i in range(len(arr)):
	cnt[arr[i]] += 1

for i in range(len(cnt)):
	for j in range(cnt[i]):
		print(i, end=' ')
