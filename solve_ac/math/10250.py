# ACM 호텔

T = int(input())

for _ in range(T):
	h, w, n = map(int, input().split())
	Y = n % h
	X = n // h + 1
	if Y == 0:
		X -= 1
		Y = h
	if X < 10:
		print("{}0{}".format(Y, X))
	else:
		print("{}{}".format(Y, X))