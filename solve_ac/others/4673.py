# 셀프 넘버
num_set = set(range(1, 10001))
gen_set = set()
for i in range(1, 10001):
	for j in str(i):
		i += int(j)
	gen_set.add(i)
self_num_set = num_set - gen_set
for i in sorted(self_num_set):
	print(i)