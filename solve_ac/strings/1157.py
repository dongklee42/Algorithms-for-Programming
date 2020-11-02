# 단어 공부
string = str(input())
alpha = "abcdefghijklmnopqrstuvxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
visited = [0] * (26 * 2)

for i in range(len(string)):
	for j in range(len(alpha)):
		if string[i] == alpha[j]:
			visited[j] += 1
			break
check = []
for i, _ in enumerate(visited):
	if visited[i] == max(visited):
		check.append(i)

for i in check:
	if len(check) > 1:
		print('?')
		break
	if visited[i] == max(visited) and i <= 25:
		print(alpha[i + 25])
	else:
		print(alpha[i])