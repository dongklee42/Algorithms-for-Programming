# 손익분기점

a, b, c = map(int, input().split())
bep = 1
while (True):
	if (a + (b * bep)) < (c * bep):
		break
	else:
		bep += 1
print(bep)