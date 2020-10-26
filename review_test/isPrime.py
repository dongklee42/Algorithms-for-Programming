# 해커랭크 소수판별 문제
# n이 소수이면 1 리턴, 아니면 나눠지는 수 중 가장 작은 수 리턴(2 이상)

n = int(input())

def	is_prime(n):
	if n <= 2:
		return 1
	for num in range(2, n, 1):
		if (n % num) == 0:
			return num
	return 1

print(is_prime(n))
