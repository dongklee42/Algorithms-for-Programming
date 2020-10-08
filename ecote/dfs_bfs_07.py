# 음료수 얼려 먹기(연결 요소 찾기 예제)

# 세로x가로 길이 저장
n, m = map(int, input().split())
print (n, m)

# 2차원 리스트 맵 정보 저장
graph = []
for i in range(n):
	graph.append(list(map(int, input())))

# DFS로 특정 노드 방문시 상하좌우 방문해보는 알고리즘
def dfs(x, y):
	# 종료조건 : 주어진 범위를 벗어나면 즉시 종료
	if (x <= -1) or (n <= x) or (y <= -1) or (y >= m):
		return False
	
	# 현재 노드를 방문 하지 않는 다면,
	if graph[x][y] == 0:
		# 해당 노드는 방문처리
		graph[x][y] = 1
		# 상, 하, 좌, 우 모든 위치들도 재귀로 호출해서 확인
		dfs(x - 1, y)
		dfs(x + 1, y)
		dfs(x, y - 1)
		dfs(x, y + 1)
		return True
	return False

# 저장된 리스트 맵 노드에 음료 채우기
result = 0
for i in range(n):
	for j in range(m):
		# 현재 위치에서 DFS 수행
		if dfs(i, j) == True:
			result += 1

# 정답 출력
print(result)
