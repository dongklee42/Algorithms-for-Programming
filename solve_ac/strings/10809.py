src = input()

alpha = "abcdefghijklmnopqrstuvwxyz"
word_list = [i for i in src]
word_num = []

for chr in alpha:
	for i in range(len(word_list)):
		if chr == word_list[i]:
			word_num.append(i)
			break
		elif i < len(word_list) - 1:
			continue
		else:
			word_num.append(-1)

for i in word_num:
	print(i, end=' ')