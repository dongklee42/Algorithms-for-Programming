# 소수 판별 문제 : 기본형

def	is_prime_number(x):
	for i in range(2, x):
		if x % i == 0:
			return False
	return True