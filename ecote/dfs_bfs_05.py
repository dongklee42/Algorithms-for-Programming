# DFS 메소드 정의
def	dfs(graph, v, visited):
	visited[v] = True
	print(v, end=' ')
	for i in graph[v]:
		if not visited[i]:
			dfs (graph, i, visited)

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

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)