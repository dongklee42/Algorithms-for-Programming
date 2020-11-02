# 단어 공부 : 숏 코드

string = input().upper()
uniq_words = list(set(string))

cnt_lst = []
for w in uniq_words:
	cnt = string.count(w)
	cnt_lst.append(cnt)

if cnt_lst.count(max(cnt_lst)) > 1:
	print('?')
else:
	max_idx = cnt_lst.index(max(cnt_lst))
	print(uniq_words[max_idx])

