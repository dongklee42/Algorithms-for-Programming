# 단어 공부 숏코딩ver
s = input().upper()
a = []
for i in range(ord('A'), (ord('Z') + 1)):
 a.append(s.count(chr(i)))
print('?'if a.count(max(a))>1 else chr(a.index(max(a))+ord('A')))