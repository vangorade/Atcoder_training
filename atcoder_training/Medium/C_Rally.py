N = int(input())
A = list(map(int, input().split()))
    
ans = 1001001001
    
mx = max(A)
mi = min(A)
    
for p in range(mi, mx + 1):
    total = 0
    for j in range(N):
        total += (A[j] - p) ** 2
    ans = min(ans, total)
    
print(ans)