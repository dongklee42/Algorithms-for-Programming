def is_prime(n):
  num = 2
  while (n > num and n > 1):
    if n % num == 0:
      return 0
    else:
      num += 1
  return 1

N = int(input())
num_list = list(map(int, input().split()))
cnt = 0

for i in range(N):
  if is_prime(num_list[i]) == 1:
    cnt += 1
print(cnt)
