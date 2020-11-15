# 하노이 탑 : 재귀 함수
from sys import *
setrecursionlimit(10**6)

N = int(input())
result = []

def move(sp, ap):
	global result
	result.append((sp, ap))

def hanoi(n, a, b, c):
	if n == 1:
		move(a, b)
		return
	hanoi(n - 1, a, c, b)
	move(a, c)
	hanoi(n - 1, b, a, c)

hanoi(N, 1, 2, 3)
print(len(result))
for a, c in result:
	print(a, c)