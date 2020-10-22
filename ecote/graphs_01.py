## 기타 그래프 이론 : 개선된 서로소 집합 기본구조(경로 압축 기법)

def	find_parent(parent, x):
	if parent[x] != x:
		parent[x] = find_parent(parent, parent[x])
	return parent[x]


# # 기존 함수
# def	find_parent(parent, x):			# 특정 원소가 속한 집합을 재귀호출하여 찾기
# 	if parent[x] != x:				# 루트 노드를 찾을 때까지 재귀 호출
# 		return find_parent(parent, parent[x])
# 	return x