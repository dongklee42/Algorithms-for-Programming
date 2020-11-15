# Alpha Centauri

N = int(input())
for _ in range(N):
    x, y = map(int, input().split())
    far = (y - x)
    count = 0
    move = 1
    move_plus = 0
    while move_plus < far :
        count += 1
        move_plus += move
        if count % 2 == 0 :
            move += 1  
    print(count)