# 팩토리얼 : n = n * (n - 1)!

n = int(input())
def recur_factorial(n):
	if n <= 0 and n < 2:
		return 1
	else:
		return n * recur_factorial(n - 1)
print(recur_factorial(n))