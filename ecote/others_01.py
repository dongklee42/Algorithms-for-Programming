# 소수 판별 문제 : 제곱근 활용
import math

def is_prime_number(x):
	for i in range(2, int(math.sqrt(x)) + 1):
		if x % i == 0:
			return False
	return True
