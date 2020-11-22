# 네 번째 점

x_list = []
y_list = []
result = []
for _ in range(3):
	x, y = map(int, input().split())
	x_list.append(x)
	y_list.append(y)
for i in x_list:
	if x_list.count(i) == 1:
		result.append(i)
for i in y_list:
	if y_list.count(i) == 1:
		result.append(i)
print(result[0], result[1])