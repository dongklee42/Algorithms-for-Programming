# 그룹단어 체커
cnt = 0
for i in range(int(input())):
	word = input()
	if list(word) == sorted(word, key=word.find):
		cnt += 1
print(cnt)
