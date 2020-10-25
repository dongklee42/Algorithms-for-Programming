# 문자열 반복
cnt = int(input())
case = []

for i in range(cnt):
	iter, words = map(str, input().split())
	case.append((int(iter), words))

for i, (iter, words) in enumerate(case):
	for w in words:
		for j in range(iter):
			print(w, end='')
	print()