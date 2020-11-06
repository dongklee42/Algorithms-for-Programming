# 크로아티아 알파벳

line = input()
cro_al = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
for cro in cro_al:
	line = line.replace(cro, '_')
print(len(line))