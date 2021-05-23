n = int(input())
arr = list(map(int, input().split()))

counts = [0]*(10**5 + 10)

for i in arr:
    counts[i] += 1
    counts[i+1] += 1
    counts[i-1] += 1
print(max(counts))