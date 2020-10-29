# 투 포인터 : 리스트에 순차 접근할 때, 두 개의 점 위치를 기혹하면서 처리

n, m = map(int, input().split())
data = list(map(int, input().split()))

count = 0
interval_sum = 0
end = 0

for start in range(n):
	while (interval_sum < m) and (end < n):
		interval_sum += data[end]
		end += 1
	if interval_sum == m:
		count += 1
	interval_sum -= data[start]

print (count)