# 골드바흐의 추측 : 2보다 큰 모든 짝수는 두 소수의 합으로 나타난다.

def is_prime(m, n):
	check = [True] * (n + 1)
	sqrt_n = int(n ** 0.5)
	for i in range(2, (sqrt_n + 1)):
		if i < 2:
			check[i] = False
		if check[i] == True:
			for j in range((i + i), n + 1, i):
				check[j] = False
	result = [i for i in range(m, n + 1) if check[i] == True]
	return result

for _ in range(int(input())):
	n = int(input())
	prime_list = is_prime(1, n)
	result = []
	for i in range(len(prime_list)):
		for j in range(len(prime_list)):
			if prime_list[i] + prime_list[j] == n:
				result.append((prime_list[i], prime_list[j]))
	final = []
	for a, b in result:
		if a < b and b % 2 == 1:
			final.append((a, b))
	print(final[-1][0], final[-1][1])