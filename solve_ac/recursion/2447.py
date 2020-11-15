# 별 찍기-10(N x N)

N = int(input())
pattern = ["***", "* *", "***"]
def recur_print(n, pattern):
	if n % 3 == 0:
		print(pattern[0] * (n // 3), end='\n')
	elif n % 3 == 1:
		print(pattern[1] * (n // 3), end='\n')
	elif n % 3 == 2:
		print(pattern[2] * (n // 3), end='\n')
	
for i in range(N):
	recur_print(i, pattern)