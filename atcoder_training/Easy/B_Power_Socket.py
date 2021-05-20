A, B = map(int, input().split(' '))
cnt = 1
total = A
while(1):
    if B == 1:
        print(0)
        exit()
    if(total >= B):
        print(cnt)
        exit()
    cnt += 1 
    total += A-1