# 직사각형에서 탈출

def min_route(x, y, w, h):
	hori = w - x
	vert = h - y
	return min(hori, vert, x, y)

x, y, w, h = map(int, input().split())
print(min_route(x, y, w, h))