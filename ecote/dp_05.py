# 다이나믹 프로그래밍 : 효율적인 화폐 구성

# 정수 n, m
n, m = map(int, input().split())

# n개의 화폐 단위
arr = []
for i in range(n):
	arr.append(int(input()))

# 한 번 계산된 결과를 저장하기 위한 dp 테이블 초기화
dp_table = [10001] * (m + 1)

dp_table[0] = 0
for i in range(n):		# i == 각각의 화폐 단위
	for j in range(arr[i], m + 1):		# j == 각각의 금액
		if dp_table[j - arr[i]] != 10001:
			dp_table[j] = min(dp_table[j], (dp_table[j - arr[i]] + 1))

# 계산된 결과 출력
if dp_table[m] == 10001:
	print(-1)
else:
	print(dp_table[m])
