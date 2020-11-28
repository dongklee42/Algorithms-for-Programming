# 터렛 : 두 원의 교점 개수 찾기

for _ in range(int(input())):
	x1, y1, r1, x2, y2, r2 = map(int, input().split())
	r = ((x1 - x2) ** 2 + (y1 - y2) ** 2) **(0.5)
	r_list = [r1, r2, r]
	m = max(r_list)
	r_list.remove(m)
	if r == 0 and r1 == r2:
		print(-1)
	elif r == r1 + r2 or m == sum(r_list):
		print(1)
	elif m > sum(r_list):
		print(0)
	else:
		print(2)