# 종료조건을 포함한 재귀함수 예제
def recursive_func(idx) :
	if idx == 10 :
		return
	print(idx, "번 째 재귀함수에서", (idx + 1), "번 째 재귀함수를 호출한다.")
	recursive_func(idx + 1)
	print(idx, "번 째 재귀함수를 종료.")

recursive_func(1)