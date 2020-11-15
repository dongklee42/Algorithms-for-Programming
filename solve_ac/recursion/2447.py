# 별 찍기-10(N x N)

n = int(input())
pattern = ["***", "* *", "***"]

def recur_stars(pattern):
	matrix = []
	for i in range(3 * len(pattern)):
		if i // len(pattern) == 1:
			matrix.append(pattern[i % len(pattern)]
							+ " " * len(pattern)
							+ pattern[i % len(pattern)])
		else:
			matrix.append(pattern[i % len(pattern)] * 3)
	return list(matrix)
	
iter = 0
while (n != 3):
	n = int(n / 3)
	iter += 1

for i in range(iter):
	pattern = recur_stars(pattern)
for i in pattern:
	print(i)