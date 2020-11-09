# 달팽이는 올라가고 싶다(while 문은 시간초과)

a, b, v = map(int, input().split())
if (v - b) % (a - b) != 0:
	print(((v - b) // (a - b)) + 1)
else:
	print((v - b) // (a - b))