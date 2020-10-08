# BFS 미로 탈출 예제
from collections import deque

# 세로x가로 길이 저장
n, m = map(int, input().split())

# 2차원 리스트 맵 저장
graph = []
for i in range(n):
	graph.append(list(map(int, input())))

# 이동할 상하좌우 방향 미리 정의하기
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
	# 큐 구현을 위한 라이브러리 사용
	queue = deque()
	queue.append((x,y))

	# 큐가 빌 때 까지 반복
	while queue:
		x, y = queue.popleft()

		# 현재 위치에서 네 방향 위치 확인
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]

			# 미로 찾기 공간을 벗어난 경우 무시(종료 조건)
			if (nx < 0) or (nx >= n) or (ny < 0) or (ny >= m):
				continue
			# 제약 조건 : 벽 (숫자 0)인 경우
			if graph[nx][ny] == 0:
				continue

			# 최단거리일 때만 거리 기록
			if graph[nx][ny] == 1:
				graph[nx][ny] = graph[x][y] + 1
				queue.append((nx, ny))

	# 가장 오른쪽 아래까지 최단 거리 리턴
	return graph[n - 1][m - 1]

# 결과출력
print(bfs(0, 0))