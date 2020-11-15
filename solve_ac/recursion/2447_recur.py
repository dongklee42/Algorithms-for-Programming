# 별 찍기 : 재귀

def concat(r1, r2):
	return [''.join(x) for x in zip(r1, r2, r1)]

def recur_star(n):
	if n == 1:
		return ['*']
	n //= 3
	x = recur_star(n)
	a = concat(x, x)
	b = concat(x, [' ' * n] * n)
	return a + b + a

print('\n'.join(recur_star(int(input()))))