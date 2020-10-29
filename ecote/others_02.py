# 소수 판별 문제 : 에라토스테네스의 체
import math

n = 1000
arr = [True for _ in range(n + 1)]

# 에라토스테네스의 체
for i in range(2, int(math.sqrt(n)) + 1):
	if arr[i] == True:				# i 가 소수일 때
		j =  2						# i 를 제외한 i의 모든 배수를 지우기
		while (i * j <= n):			# n 보다 커지기 전까지 j를 더하면서 배수 지우기
			arr[i * j] = False
			j += 1