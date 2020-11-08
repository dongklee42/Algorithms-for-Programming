# 달팽이는 올라가고 싶다(while 문은 시간초과)

a, b, v = map(int, input().split())
cnt = 0
while v != 0:
	v -= a
	cnt += 1
	if v == 0:
		break
	v += b
print(cnt)