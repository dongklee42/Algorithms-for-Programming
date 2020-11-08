# 벌집 : 재귀활용(수학적인 패턴 찾는게 중요했음)
import sys

sys.setrecursionlimit(10**5)
N = int(input())
def bee_chr(N, cnt):
	if N <= 1:
		print(cnt)
		return
	else:
		bee_chr(N - (6 *cnt), cnt + 1)
bee_chr(N, 1)
