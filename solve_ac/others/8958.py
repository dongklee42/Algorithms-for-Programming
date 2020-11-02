# OX 퀴즈
n = int(input())

for _ in range(n):
	a = input()
	sum, cnt = 0, 0
	for j in range(len(a)):
		if a[j] == 'X':
			cnt = 0
		elif a[j] == 'O':
			cnt += 1
			sum += cnt
	print(sum)
