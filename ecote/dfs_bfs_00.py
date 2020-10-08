# 스택 stack 예제
stack = []

stack.append(5)			# 별도의 라입브러리로 구현하지 않아도 된다.
stack.append(2)
stack.append(3)
stack.append(7)

stack.pop()

stack.append(4)
stack.append(1)
stack.pop()

print(stack)
print(stack[ : : -1])	#최상단 원소부터 출력(reversed)