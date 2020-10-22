# 기타 그래프 이론 : 서로소 집합 기본구조

def	find_parent(parent, x):			# 특정 원소가 속한 집합을 재귀호출하여 찾기
	if parent[x] != x:				# 루트 노드를 찾을 때까지 재귀 호출
		return find_parent(parent, parent[x])
	return x

def	union_parent(parent, a, b):
	a = find_parent(parent, a)		# 각각 노드의 부모를 찾기
	b = find_parent(parent, b)
	if a < b:						# 더 큰 쪽이 작은 쪽을 부모로 설정할 수 있도록 변환
		parent[b] = a
	else:
		parent[a] = b


v, e = map(int, input().split())	# 노드의 개수 및 간선(union 연산)의 개수 입력 받기
parent = [0] * (v + 1)				# 부모테이블 0 값으로 초기화

for i in range(1, v + 1):			# 부모 테이블 상에서, 부모를 자기 자신으로 초기화
	parent[i] = i


# union 연산을 각각 수행
for i in range(e):
	a, b = map(int, input().split())
	union_parent(parent, a, b)

# 각 원소가 속한 집합 출력
print("각 원소가 속한 집합 : ", end=' ')
for i in range(1, (v + 1)):
	print(find_parent(parent, i), end=' ')

print()

# 부모 테이블 내용 출력하기
print("부모 테이블 : ", end=' ')
for i in range(1, (v + 1)):
	print(parent[i], end=' ')