# 다이얼 누르는 시간 재기

al_num = input()
dial = ["", "1","ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ", "0"]
sum = 0
for a in al_num:
	for i, j in enumerate(dial):
		if a in j:
			sum += (1 + i)
print(sum)