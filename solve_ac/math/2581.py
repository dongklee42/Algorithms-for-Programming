from math import sqrt

def is_prime(n):
  num = 2
  if n < 2:
    return 0
  while sqrt(n) > num:
    if n % num == 0:
      return 0
    else:
      num += 1
  return 1

m = int(input())
n = int(input())
min_prime = []
sum_prime = 0
for i in range(m, (n + 1)):
  if is_prime(i) == 1:
    sum_prime += i
    min_prime.append(i)
if sum_prime == 0:
  print(-1)
else:
  print(sum_prime)
  print(min(min_prime))
