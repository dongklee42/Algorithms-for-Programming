# 다이나믹 프로그래밍 : 기본적인 피보나치 코드(재귀, 메모이제이션)
d = [0] * 100

def recursive_fibo(x):
	# 어떤 함수가 호출되고 있는지 확인하기
	print("f(" + str(x) + ")", end = ' ')

	# 종료 조건
	if x == 1 or x == 2:
		return 1
	# 이미 계산한 적이 있는 문제라면 그대로 반환
	if d[x] != 0:
		return d[x]
	# 아직 계산하지 않은 문제라면 점화식에 따른 피보나치 결과 반환
	d[x] = recursive_fibo(x - 1) + recursive_fibo(x - 2)
	return d[x]

print(recursive_fibo(6))