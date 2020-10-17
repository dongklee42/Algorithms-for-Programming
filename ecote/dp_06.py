# 다이나믹 프로그래밍 : 금광

# 테스트 케이스 입력
for tc in range(int(input())):
	# 데이터 입력
	n, m = map(int, input().split())
	arr = list(map(int, input().split()))

	# arr가 1차원 데이터로 들어오기 때문에 dp 테이블에 2차원 형식으로 
	dp = []
	idx = 0
	for i in range(n):
		dp.append(arr[idx : (idx + m)])
		idx += m
	
# print(dp)

	# 다이나믹 프로그래밍 진행
	for j in range(1, m):
		for i in range(n):
			# 왼쪽 위에서 오는 경우
			if i == 0:
				left_up = 0
			else:
				left_up = dp[i - 1][j - 1]
			# 왼쪽 아래서 오는 경우
			if i == (n - 1):
				left_down = 0
			else:
				left_down = dp[i + 1][j - 1]
			# 왼쪽에서 오는 경우
			left = dp[i][j - 1]
			dp[i][j] = dp[i][j] + max(left_up, left_down, left)

	result = 0
	for i in range(n):
		result = max(result, dp[i][m - 1])
	print(result)
