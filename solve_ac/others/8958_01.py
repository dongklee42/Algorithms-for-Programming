# 8958 숏코딩

N=int(input())
for _ in range(N):
    print(sum([int(len(x)*(len(x)+1)/2) for x in input().split('X')]))
