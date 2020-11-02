# 평균은 넘겠지
N = int(input())

for _ in range(N):
	data = list(map(int, input().split()))
	num = data[0]
	cnt = 0
	avg = sum(data[1:]) / num
	for i in range(1, len(data)):
		if data[i] > avg:
			cnt += 1
	print(str("%.3f" % round(cnt / num * 100, 3)) + '%')
	# print("{}%".format(round((cnt / num * 100), 3)))