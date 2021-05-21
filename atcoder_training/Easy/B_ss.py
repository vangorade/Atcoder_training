S = input()
ans = 0
s = S
for i in range(1,len(S)):
    s = S[:-i] # pop last char 
    if s[:len(s)//2] == s[len(s)//2:]:
        ans = len(s)
        break
print(ans)

# #sol2

# S = input()
# N = len(S)
    
# ans = 0
# for i in range(N-2, 1, -2):
#     mid = (i+1) // 2
#     if S[0:mid] == S[mid:i]:
#         print(len(S[:i]))
#         break