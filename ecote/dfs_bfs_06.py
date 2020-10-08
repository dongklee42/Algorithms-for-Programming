# BFS 너비우선탐색 예제
from collections import deque

def bfs(graph, start, visited):
	queue = deque([start])		# 큐 라이브러리 사용
	visited[start] = True		# 현재 노드 방문 처리
	
	# 큐가 빌 때 까지 반복
	while queue:
		v = queue.popleft()		# 큐에서 하나의 원소를 뽑아 출력
		print(v, end=' ')

		for i in graph[v]:		# 아직 방문하지 않은 인접 원소들을 큐에 삽입
			if not visited[i]:
				queue.append(i)
				visited[i] = True

# 노드 정보 표현(인접리스트 방식)
graph = [
	[],				# 보통 1번 노드에서 시작하기 때문에 비워 둠
	[2, 3, 8],
	[1, 7],
	[1, 4, 5],
	[3, 5],
	[3, 4],
	[7],
	[2, 6, 8],
	[1, 7]
]

# 각 노드가 방문된 정보를 표현(1차원 리스트)
visited = [False] * 9

# 정의된 bfs 함수 사용
bfs(graph, 1, visited)