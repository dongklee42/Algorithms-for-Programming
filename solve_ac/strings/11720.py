# 숫자의 합
n = int(input())
num_str = input()
result = 0
for i in range(n):
	result += int(num_str[i])

print(result)