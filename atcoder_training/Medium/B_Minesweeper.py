h,w = map(int,input().split())
A = [[]for i in range(h)]
# all 8 dir
dx = [1,1,0,-1,-1,-1,0,1]
dy = [0,1,1,1,0,-1,-1,-1]
for j in range(h):
    A[j] = list(input())
    
for y in range(h):
    for x in range(w):
        if A[y][x] == '.':
            count = 0
            for i in range(8):
                x1 = x + dx[i]
                y1 = y + dy[i]
                if 0 <= x1 < w and 0 <= y1 < h and A[y1][x1] == '#':
                    count += 1
                A[y][x] = count
        
for i in range(h):
    a = map(str, A[i])
    print("".join(a))