# 다이나믹 프로그래밍 : 기본적인 피보나치 코드(재귀)
def recursive_fibo(x):
	if x == 1 or x == 2:
		return 1
	return (recursive_fibo(x - 1) + recursive_fibo(x - 2))

print(recursive_fibo(6))