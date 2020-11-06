# 거꾸로 읽는 수
a, b = input().split()

def rev_str(word):
	rev_word = ""
	for i in reversed(range(len(word))):
		rev_word += word[i]
	return rev_word

a = rev_str(a); b = rev_str(b)
print(max(a, b))