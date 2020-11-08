# 설탕 배달

N = int(input())
def sugar(N):
	for b in range((N // 3) + 1):
		for a in range((N // 5) + 1):
			if (5 * a) + (3 * b) == N:
				return a + b
	return -1
print(sugar(N))

