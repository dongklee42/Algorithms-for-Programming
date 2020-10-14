# 떡볶이 길이 문제 : Parametric search
n, m = list(map(int, input().split(' ')))
arr = list(map(int, input().split()))

# 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(arr)		# 가장 큰 길이

# 이진탐색 수행
result = 0
while (start <= end):
	total = 0
	mid = (start + end) // 2
	for x in arr:
		# 잘랐을 때 떡의 양 계산
		if x > mid:
			total += x - mid
	# 떡의 양이 부족한 경우 더 많이 자르기(왼쪽 부분 탐색)
	if total < m:
		end = mid - 1
	# 떡의 양이 충분한 경우 덜 자르기(오른쪽 부분 탐색)
	else:
		result = mid			# 최대한 덜 잘랐을 때가 정답. 여기에 결과 기록
		start = mid + 1

print(result)