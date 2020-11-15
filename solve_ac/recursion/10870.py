# 피보나치 : 0 1 1 2 3 5...

n = int(input())
def recur_fibonacci(n):
	if n <= 1:
		return n
	else:
		return recur_fibonacci(n - 1) + recur_fibonacci(n - 2)
print(recur_fibonacci(n))