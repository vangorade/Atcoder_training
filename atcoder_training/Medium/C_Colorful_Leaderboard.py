n = int(input())
arr = list(map(int, input().split()))

color_cnt = [0]*8
cnt = 0

for i in arr:
    if i >= 3200:
        cnt += 1
    else:
        color_cnt[i//400] = 1

ans = color_cnt.count(1)
if ans == 0:
    print(1, cnt)
else:
    print(ans, ans + cnt)
