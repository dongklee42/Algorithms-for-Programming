# 기타 그래프 이론 : 신장 트리 알고리즘

def	find_parent(parent, x):			# 특정 원소가 속한 집합 찾기
	if parent[x] != x:
		parent[x] = find_parent(parent, parent[x])
	return parent[x]

def union_parent(parent, a, b):		# 두 원소가 속한 집합을 합치기
	a = find_parent(parent, a)
	b = find_parent(parent, b)
	if a < b:
		parent[b] = a
	else:
		parent[a] = b

v, e = map(int, input().split())
parent = [0] * (v + 1)

# 모든 간선을 담을 리스트와, 최종비용을 담을 변수
edges = []
result = 0

# 모든 부모를 자기 자신으로 초기화
for i in range(1, (v + 1)):
	parent[i] = i

# 모든 간선정보 입력받기
for _ in range(e):
	a, b, cost = map(int, input().split())
	edges.append((cost, a, b))		# 비용 순으로 정렬하기 위해서, 튜플의 첫 원소를 비용으로 설정

# 간선을 비용 순으로 정렬
edges.sort()

# 간선을 하나씩 확인하며 사이클이 발생하지 않는 경우 집합에 포함
for edge in edges:
	#print(edge)
	cost, a, b = edge
	if find_parent(parent, a) != find_parent(parent, b):
		union_parent(parent, a, b)
		result += cost

print(result)