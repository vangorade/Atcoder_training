s = str(input())
len_s = len(s)
#BBW b = 2, at idx 2= W so, cnt += b
b = 0
cnt = 0

for i in range(len_s):
    if s[i] == 'W':
        cnt += b
    else:
        b += 1
print(cnt)