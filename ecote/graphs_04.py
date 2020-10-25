# 기타 그래프 알고리즘 : 위상 정렬 알고리즘

from collections import deque

v, e = map(int, input().split())

indegree = [0] * (v + 1)				# 모든 노드에 대한 진입차수 0 초기화
graph = [[] for i in range(v + 1)]		# 각 노드에 연결된 간선정보를 담은 링크드리스트

print("graph : ", graph)

for _ in range(e):
	a, b = map(int, input().split())
	graph[a].append(b)
	indegree[b] += 1

print("indegree : ", indegree)
print("graph : ", graph)

def	topology_sort():
	result = []
	q = deque()
	for i in range(1, (v + 1)):
		if indegree[i] == 0:
			q.append(i)
	while q:
		now = q.popleft()
		result.append(now)
		for i in graph[now]:
			indegree[i] -= 1
			if indegree[i] == 0:
				q.append(i)
	
	# 결과 출력
	for i in result:
		print(i, end=' ')

topology_sort()