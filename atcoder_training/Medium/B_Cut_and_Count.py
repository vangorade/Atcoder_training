# str -> aabbca 

# a  abbca  1
# aa  bbca  1
# aab  bca  2 max=2
# aabb  ca  1
# aabbc  a  1

# import collections

# n = int(input())
# s = input()
# ans = 0
# for i in range(n):
#     count = 0
#     cut1= list(s[0:i])
#     cut2 = list(s[i:n])
#     count_cut1=collections.Counter(cut1)
#     count_cut2=collections.Counter(cut2)
#     for i in range(len(list(count_cut2.keys()))):
#         if list(count_cut2.keys())[i] in list(count_cut1.keys())[i]:
#             count += 1
#     ans = max(ans, count)
# print(ans)

N = int(input())
S = list(input())
flg = []
ans = -float('inf')
 
for i in range(1, N):
    a = set(S[:i])
    b = set(S[i:])
    # print(a, b)
    cnt = 0
    for j in a:
        if j in b:
            cnt += 1
    ans = max(ans, cnt)
print(ans)