# 큐 Queue 예제
from collections import deque

# 큐를 구현하기 위해서는 'deque' 라이브러리를 가져와야 한다.
queue = deque()

queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)

queue.popleft()

queue.append(5)
queue.append(6)

queue.popleft()

print(queue)	#들어온대로 출력

queue.reverse()	#역순으로 바꾸어 저장
print(queue)

# deque 객체를 리스트 자료형으로 변경 시
print(list(queue))