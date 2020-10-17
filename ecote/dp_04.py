# 다이나믹 프로그래밍 : 개미 전사
n = int(input())
k_arr = list(map(int, input().split()))

dp_table = [0] * 100

# bottom-up 방식의 다이나믹 프로그래밍 진행
dp_table[0] = k_arr[0]
dp_table[1] = max(k_arr[0], k_arr[1])

# 3번째 항부터 점화식 진행
for i in range(2, n):
	dp_table[i] = max(dp_table[i - 1], (dp_table[i - 2] + k_arr[i]))

# 계산된 결과 출력
print(dp_table[n - 1])