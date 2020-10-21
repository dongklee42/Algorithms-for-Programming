# 최단 경로 알고리즘 : 힙 Heap 자료구조 (최대 힙)
import heapq

# 오름차운 힙 정렬(Heap sort)
def	heapsort(iterable):
	h = []
	result = []

	for value in iterable:			# 모든 원소를 차례대로 힙에 삽입
		heapq.heappush(h, -value)
	for _ in range(len(h)):			# 힙에 삽입된 원소를 차례대로 꺼내어 담기
		result.append(-heapq.heappop(h))
	return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)