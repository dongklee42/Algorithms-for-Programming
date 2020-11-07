# 손익분기점 : 반복문 피해서 작성하기

a, b, c = map(int, input().split())
bep = 0
if c <= b:
	bep = -1
else:
	bep = a // (c - b) + 1
print(bep)