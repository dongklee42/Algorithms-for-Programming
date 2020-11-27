# 베르트랑 공준 : 소수판별 활용 문제

def is_prime(m, n):
	check = [True] * (n + 1)
	sqrt_n = int(n ** 0.5)
	for i in range(sqrt_n + 1):
		if i < 2:
			check[i] = False
		if check[i] == True:
			for j in range((i + i), n + 1, i):
				check[j] = False
	result = [i for i in range(m + 1, n + 1) if check[i] == True]
	return len(result)

while True:
	n = int(input())
	if n == 0:
		break
	print(is_prime(n, (2 * n)))