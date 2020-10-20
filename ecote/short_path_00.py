# 최단 경로 알고리즘 : Dijkstra 방식
import sys

# 데이터 입력
data = sys.stdin.readline
INF = int(1e9)						# 무한을 의미하는 ls값으로 10억을 설정
n, m = map(int, input().split())	# 노드 개수 n, 간선의 개수 m 입력 받기
start = int(input())				# 시작 노드 번호 입력받기
graph = [[] for i in range(n + 1)]	# 각 노드의 간선 정보(거리) 리스트 만들기
visited = [False] * (n + 1)			# 방문 한적 있는지 여부를 체크하는 리스트 만들기 + 초기화
distance = [INF] * (n + 1)			# 최단 거리 테이블을 모두 무한으로 초기화

for _ in range(m):					# 모든 거리 입력 받기
	a, b, c = map(int, input().split())
	graph[a].append((b, c))			# a번 노드가 b노드 로 가는 거리가 c 라는 의미

# # 확인 출력
# print("graph : ", graph)
# print("visited : ", visited)
# print("distance : ", distance)

# 방문하지 않은 노드 중, 최단 거리 노드 번호를 리턴하는 함수
def	get_smallest_node():
	min_value = INF
	idx = 0					# 최단거리 노드의 인덱스
	for i in range(1, (n + 1)):
		if distance[i] < min_value and not visited[i]:
			min_value = distance[i]
			idx = i
	return idx

# 다익스트라 알고리즘 함수
def	dijkstra(start):
	distance[start] = 0					# 시작 노드에 대해 초기화
	visited[start] = True
	for j in graph[start]:
		# print("j[0] : {}, j[1] : {}".format(j[0], j[1]))	# 거리가 어떻게 초기화 되는지 잠시 확인~
		distance[j[0]] = j[1]
	
	for _ in range(n - 1):
		now = get_smallest_node()		# 현재 노드에서 최단 거리 노드를 꺼내 방문처리
		visited[now] = True
		for j in graph[now]:			# 현재 노드와 연결된 다른 노드 확인
			cost = distance[now] + j[1]
			if cost < distance[j[0]]:	# 현재 노드를 거쳐 다른 노드로 이동하는 거리가 더 짧은 경우
				distance[j[0]] = cost

# 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리 출력
for i in range(1, (n + 1)):
	if distance[i] == INF:
		print("INFINITY")
	else:
		print(distance[i])