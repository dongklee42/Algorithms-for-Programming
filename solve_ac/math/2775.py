# 부녀회장이 될테야

T = int(input())
for _ in range(T):
	k = int(input())
	n = int(input())
	home = [h for h in range(1, n + 1)]
	for i in range(k):
		for j in range(1, n):
			home[j] += home[j - 1]
	print(home[n - 1])