# 소수 : 에라토스테네스 체

def is_prime(m, n):
	check = [True] * (n + 1)
	sqrt_n = int(n ** 0.5)
	for i in range(2, (sqrt_n + 1)):
		if check[i] == True:
			for j in range((i + i), n + 1, i):
				check[j] = False
	result = [i for i in range(m, n + 1) if check[i] == True]
	return result

m, n = map(int, input().split())
for i in is_prime(m, n):
	print(i)