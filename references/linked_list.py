
# 출처 : https://velog.io/@johnque/Python-LinkedList
class Node:
	def __init__(self, data, next=None):
		self.data = data
		self.next = next

class LinkedList:
	def __init__(self, data):
		self.head = Node(data)

	def add(self, data):
		if self.head == '':
			self.head = Node(data)
		else:
			node = self.head
			while node.next:
				node = node.next
			node.next = Node(data)